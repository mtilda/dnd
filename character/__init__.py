import bisect
import functools

from typing_extensions import Self

from character.classifications.barbarian import Barbarian
from character.classifications.bard import Bard
from character.classifications.cleric import Cleric
from character.classifications.druid import Druid
from character.classifications.fighter import Fighter
from character.classifications.monk import Monk
from character.classifications.paladin import Paladin
from character.classifications.ranger import Ranger
from character.classifications.rogue import Rogue
from character.classifications.sorcerer import Sorcerer
from character.classifications.warlock import Warlock
from character.classifications.wizard import Wizard
from character.race import Race
from character.races.dragonborn import Dragonborn
from character.races.elf import Elf
from character.races.gnome import Gnome
from character.races.half_elf import HalfElf
from character.races.half_orc import HalfOrc
from character.races.halfling import Halfling
from character.races.human import Human
from character.races.orc import Orc
from character.races.tiefling import Tiefling
from models.entity import Entity

_classifications: list[type[Race]] = [
    Barbarian,
    Bard,
    Cleric,
    Druid,
    Fighter,
    Monk,
    Paladin,
    Ranger,
    Rogue,
    Sorcerer,
    Warlock,
    Wizard,
]

_races: list[type[Race]] = [
    Dragonborn,
    Elf,
    Gnome,
    HalfElf,
    HalfOrc,
    Halfling,
    Human,
    Orc,
    Tiefling,
]


class CharacterMeta(type):
    templated_fields = {
        ("hit_die", "Hit Die"),
        ("primary_ability", "Primary Ability"),
        ("saving_throw_proficiencies", "Saving Throw Proficiencies"),
    }

    def __new__(cls: type[Self], name: str, bases: tuple[type], attrs: dict) -> Self:
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        for base in bases:
            print(base.__name__)
            print(base.__dict__)
        return super().__new__(cls, name, bases, attrs)


class Character(Entity):
    _advancement_table: list[tuple[str, str, str]] = [
        (0, 1, 2),
        (300, 2, 2),
        (900, 3, 2),
        (2700, 4, 2),
        (6500, 5, 3),
        (14000, 6, 3),
        (23000, 7, 3),
        (34000, 8, 3),
        (48000, 9, 4),
        (64000, 10, 4),
        (85000, 11, 4),
        (100000, 12, 4),
        (120000, 13, 5),
        (140000, 14, 5),
        (165000, 15, 5),
        (195000, 16, 5),
        (225000, 17, 6),
        (265000, 18, 6),
        (305000, 19, 6),
        (355000, 20, 6),
    ]

    @property
    def classification(self):
        obj = self._Classification()
        obj.name = self._Classification.__name__
        return obj

    @property
    def race(self):
        obj = self._Race()
        obj.name = self._Race.__name__
        return obj

    def __init__(self, class_name: str, race_name: str, xp: int = 0, **kwargs):
        self.xp = xp
        matching_classifications = [
            CC for CC in _classifications if CC.__name__ == class_name
        ]
        self._Classification = matching_classifications[0]

        matching_races = [RR for RR in _races if RR.__name__ == race_name]
        self._Race = matching_races[0]
        self._Race = matching_races[0]
        super().__init__(**kwargs)
        self.log.info("Creating character: %s", self)

    @functools.cache
    def get_advancement_row(self, xp):
        index = bisect.bisect_left(
            Character._advancement_table, xp, key=lambda x: x[0]
        )
        if index:
            return Character._advancement_table[index]
        raise ValueError

    @property
    def level(self):
        row = self.get_advancement_row(self.xp)[1]
        return row

    def __str__(self):
        return "%s -- level %s %s %s" % (
            self.name,
            self.level,
            self.race.name,
            self.classification.name,
        )

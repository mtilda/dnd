from character.classification import Classification
from dice import d8


class Bard(Classification):
    "An inspiring magician those whose power echoes the music of creation."
    hit_die = d8
    primary_ability = {"Charisma"}
    saving_throw_proficiencies = {"Dexterity", "Charisma"}

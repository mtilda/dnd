from character.classification import Classification
from dice import d10


class Ranger(Classification):
    "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization."
    hit_die = d10
    primary_ability = {"Dexterity", "Wisdom"}
    saving_throw_proficiencies = {"Strength", "Dexterity"}

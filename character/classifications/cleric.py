from character.classification import Classification
from dice import d8


class Cleric(Classification):
    "A priestly champion who wields divine magic in service of a higher power."
    hit_die = d8
    primary_ability = {"Wisdom"}
    saving_throw_proficiencies = {"Wisdom", "Charisma"}

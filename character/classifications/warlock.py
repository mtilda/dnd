from character.classification import Classification
from dice import d8


class Warlock(Classification):
    "A wielder of magic that is derived from a bargain with an extraplanar entity."
    hit_die = d8
    primary_ability = {"Strength"}
    saving_throw_proficiencies = {"Strength", "Consitution"}

from character.classification import Classification
from dice import d8


class Druid(Classification):
    "A priest of the Old Faith, wielding the powers of nature—moonlight and plant growth, fire and lightning—and adopting animal forms."
    hit_die = d8
    primary_ability = {"Wisdom"}
    saving_throw_proficiencies = {"Intelligence", "Wisdom"}

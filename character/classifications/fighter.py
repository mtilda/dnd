from character.classification import Classification
from choice import Choice, ChosableFieldsMeta
from dice import d10


class Fighter(Classification, metaclass=ChosableFieldsMeta):
    "A master of martial combat, skilled with a variety of weapons and armor."
    hit_die = d10
    primary_ability = Choice(1, "Strength", "Dexterity")
    saving_throw_proficiencies = {"Strength", "Consitution"}

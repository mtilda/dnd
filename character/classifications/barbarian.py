from character.classification import Classification
from dice import d12


class Barbarian(Classification):
    "A fierce warrior of primitive background who can enter into a battle rage."
    hit_die = d12
    primary_ability = {"Strength"}
    saving_throw_proficiencies = {"Strength", "Consitution"}

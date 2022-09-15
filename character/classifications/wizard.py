from character.classification import Classification
from dice import d6


class Wizard(Classification):
    "A scholarly magic-user capable of manipulating the structures of reality.."
    hit_die = d6
    primary_ability = {"Charisma"}
    saving_throw_proficiencies = {"Wisdom", "Charisma"}

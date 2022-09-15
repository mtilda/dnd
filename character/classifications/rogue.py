from character.classification import Classification
from dice import d8


class Rogue(Classification):
    "A scoundrel who uses stealth and trickery to overcome obstacles and enemies."
    hit_die = d8
    primary_ability = {"Dexterity"}
    saving_throw_proficiencies = {"Dexterity", "Intelligence"}

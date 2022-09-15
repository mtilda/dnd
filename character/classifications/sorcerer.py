from character.classification import Classification
from dice import d6


class Sorcerer(Classification):
    "A spellcaster who draws on inherent magic from a gift or bloodline."
    hit_die = d6
    primary_ability = {"Charisma"}
    saving_throw_proficiencies = {"Consitution", "Charisma"}

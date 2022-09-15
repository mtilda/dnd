from character.classification import Classification
from dice import d10


class Paladin(Classification):
    "A holy warrior bound to a sacred oath."
    hit_die = d10
    primary_ability = {"Strength", "Charisma"}
    saving_throw_proficiencies = {"Wisdom", "Charisma"}

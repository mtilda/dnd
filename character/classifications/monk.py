from character.classification import Classification
from dice import d8


class Monk(Classification):
    "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection."
    hit_die = d8
    primary_ability = {"Dexterity", "Wisdom"}
    saving_throw_proficiencies = {"Strength", "Dexterity"}

from ..elements import create_air
from elements import create_fire
from alchemy.potions import strength_potion

def lead_to_gold() -> str:
    return f"Recipe transmutation Lead to Gold: '{create_air()}' "\
        f"and {strength_potion} mixed with '{create_fire()}"
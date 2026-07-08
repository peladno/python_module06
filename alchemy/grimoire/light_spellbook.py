#!/usr/bin/env python3
from .light_validator import validate_ingredients 


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validator = validate_ingredients(ingredients)

    if "INVALID" in validator:
        result = f"Spell rejected: {spell_name} ({validator})"
    else: 
        result = f"Spell recorded: {spell_name} ({validator})"
    return result

# def main() -> None:
#     word = "agua"
#     print(light_spell_record("Fantasy",word))


# if __name__ == "__main__":
#     main()

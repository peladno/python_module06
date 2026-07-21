#!/usr/bin/env python3
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validator = validate_ingredients(ingredients)

    if "INVALID" in validator:
        result = f"Spell Rejected: {spell_name} ({validator})"
    else:
        result = f"Spell recorded: {spell_name} ({validator})"
    return result

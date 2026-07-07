def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients as light

    i = ingredients
    tokens = [item.strip().casefold() for item in i.split(",") if i.strip()]
    allowed = [a.casefold() for a in light()]

    valid = any(t in allowed for t in tokens)

    if not tokens:
        formatted = "(no ingredients)"
    elif len(tokens) == 1:
        formatted = tokens[0].capitalize()
    elif len(tokens) == 2:
        formatted = f"{tokens[0].capitalize()} and {tokens[1]}"
    else:
        formatted = ", ".join(tokens[:-1]).capitalize() + f" and {tokens[-1]}"

    return f"{formatted} - {'VALID' if valid else 'INVALID'}"


def main() -> None:
    word = "earth, air, wind, water"
    print(validate_ingredients(word))


if __name__ == "__main__":
    main()

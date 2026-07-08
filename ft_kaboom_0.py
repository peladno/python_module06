#!/usr/bin/env python3

from alchemy.grimoire.light_spellbook import light_spell_record


if __name__ == "__main__":
    print("Using grimoire module directly")
    print("Testing record light spell:", light_spell_record("Fantasy", "earth, water, fire"))
    print("Testing record light spell2:", light_spell_record("Fantasia", "tierra, agua, fuego"))
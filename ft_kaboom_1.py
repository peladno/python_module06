#!/usr/bin/env python3
from alchemy.grimoire.dark_spellbook import dark_spell_record


if __name__ == "__main__":
    print("Using grimoire module directly")
    print("Testing record light spell:",
          dark_spell_record("Fantasy", "earth, water, fire"))

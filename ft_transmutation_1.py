#!/usr/bin/env python3
import alchemy.transmutation


if __name__ == "__main__":
    gold = alchemy.transmutation.recipes.lead_to_gold()
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {gold}")

import alchemy

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", alchemy.create_air())
    try:
        print(alchemy.create_earth())
    except Exception as e:
        print(e)
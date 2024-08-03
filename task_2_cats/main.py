from pathlib import Path
from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    try:
        PATH = Path(__file__).parent / path
        cats = []
        with open(PATH, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(",")
                    cats.append({"id": id, "name": name, "age": age})
                except Exception:
                    print(f"Invalid data in line: {line.strip()}")
                    continue
        return cats
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example usage
cats_info = get_cats_info("cats.txt")
print(cats_info)

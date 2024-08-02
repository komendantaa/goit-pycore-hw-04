from pathlib import Path


def get_cats_info(path: str) -> list[dict[str, str]]:
    PATH = Path(__file__).parent / path
    with open(PATH, "r", encoding="utf-8") as file:
        result = []
        for line in file.readlines():
            id, name, age = line.strip().split(",")
            result.append({"id": id, "name": name, "age": age})
        return result


cats_info = get_cats_info("cats.txt")
print(cats_info)

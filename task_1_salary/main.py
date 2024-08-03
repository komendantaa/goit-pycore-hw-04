from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    try:
        total = 0
        count = 0
        PATH = Path(__file__).parent / path

        with open(PATH, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salary = int(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Invalid data in line: {line.strip()}")
                    continue

        if count == 0:
            return (0, 0.0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0.0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0.0)


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

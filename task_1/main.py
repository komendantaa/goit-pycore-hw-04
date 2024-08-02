from pathlib import Path


def total_salary(path: str) -> tuple[int, int]:
    PATH = Path(__file__).parent / path
    with open(PATH, "r", encoding="utf-8") as file:
        min: int = None
        max: int = 0
        for line in file.readlines():
            _, salary = line.split(",")
            salary = int(salary)
            min = salary if (min == None or salary < min) else min
            max = salary if (salary > max) else max

    return (min, max)


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

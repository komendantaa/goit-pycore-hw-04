from pathlib import Path
from colorama import Fore, Back, Style
import sys

INDENT = "    "


def print_dir(name: str):
    print(f"{Fore.BLUE}{name}/")


def print_file(name: str):
    print(f"{Fore.GREEN}{name}")


def print_folder_three(dir_path: str, prefix: str = "", is_deep: bool = False):
    dir = Path(dir_path)

    if not dir.is_dir():
        return None

    if not is_deep:
        print_dir(dir.name)
        prefix = INDENT

    for subj in dir.iterdir():
        string = f"{prefix}{subj.name}"

        if subj.is_dir():
            print_dir(string)
            print_folder_three(subj, prefix + INDENT, True)
        else:
            print_file(string)


path = sys.argv[1]
print_folder_three(path)

from pathlib import Path
from colorama import Fore, init
import sys

# Initialize colorama
init(autoreset=True)

INDENT = "    "


def print_dir(name: str, prefix: str = ""):
    print(f"{prefix}{Fore.BLUE}{name}/")


def print_file(name: str, prefix: str = ""):
    print(f"{prefix}{Fore.GREEN}{name}")


def print_folder_tree(dir_path: str, prefix: str = ""):
    try:
        dir = Path(dir_path)

        if not dir.is_dir():
            print(f"{Fore.RED}Error: '{dir_path}' is not a valid directory.")
            return

        # Print root directory
        if not prefix:
            print_dir(dir.name)
            prefix = INDENT

        for subj in dir.iterdir():
            if subj.is_dir():
                print_dir(subj.name, prefix)
                print_folder_tree(subj, prefix + INDENT)
            else:
                print_file(subj.name, prefix)

    except FileNotFoundError:
        print(f"{Fore.RED}Error: The directory '{dir_path}' does not exist.")
    except PermissionError:
        print(f"{Fore.RED}Error: Permission denied to access '{dir_path}'.")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")


path = sys.argv[1]
print_folder_tree(path)

from typing import List, Tuple, Dict, Optional


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def is_args_valid(
    args: List[str], skip_phone: bool = False
) -> Tuple[bool, Optional[str]]:
    if not args or not args[0]:
        return False, "Invalid name."
    if not skip_phone and (len(args) < 2 or not args[1]):
        return False, "Invalid phone."
    return True, None


def is_exists(name: str, contacts: Dict[str, str]) -> bool:
    return name in contacts


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    is_valid, error_message = is_args_valid(args)
    if not is_valid:
        return error_message

    name, phone = args
    if is_exists(name, contacts):
        return "Contact already exists."

    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    is_valid, error_message = is_args_valid(args)
    if not is_valid:
        return error_message

    name, phone = args
    if not is_exists(name, contacts):
        return "Contact not found."

    contacts[name] = phone
    return "Contact changed."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    is_valid, error_message = is_args_valid(args, skip_phone=True)
    if not is_valid:
        return error_message

    name = args[0]
    if not is_exists(name, contacts):
        return "Contact not found."

    return contacts[name]


def delete_contact(args: List[str], contacts: Dict[str, str]) -> str:
    is_valid, error_message = is_args_valid(args, skip_phone=True)
    if not is_valid:
        return error_message

    name = args[0]
    if not is_exists(name, contacts):
        return "Contact not found."

    del contacts[name]
    return "Contact removed."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command in ["phone", "show"]:
            print(show_phone(args, contacts))
        elif command in ["delete", "remove"]:
            print(delete_contact(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

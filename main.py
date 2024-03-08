import pickle

from colorama import Fore

from classes import Employee, Staff
from functions import parse_input


def save_data(book, filename="staff.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="staff.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Staff()


def main():
    book = load_data()

    methods = {
        "ap": Employee.add_position,
        "cp": Employee.edit_position,
        "fp": Employee.find_position,
        "dp": Employee.remove_position,
        "ab": Employee.add_birthday,
        "fb": Employee.find_birthday,
        "ga": Employee.get_age,
        "de": Employee.remove_employee,
    }

    def align_commands(commands):
        lines = [command.split(" - ") for command in commands]

        max_length_first = max(len(line[0]) for line in lines)
        max_length_second = max(len(line[1]) if len(line) > 1 else 0 for line in lines)

        formatted_commands = [
            (
                f"{line[0]:<{max_length_first}} | {line[1]:<{max_length_second}}"
                if len(line) > 1
                else line[0]
            )
            for line in lines
        ]

        hyphen_line = f"{'-' * max_length_first} | {'-' * max_length_second}"

        formatted_with_lines = [f"{line}\n{hyphen_line}" for line in formatted_commands]

        return "\n".join([hyphen_line] + formatted_with_lines[:-1])

    commands_list = [
        "ap/[name]/[position] - add position",
        "cp/[name]/[old_position]/[new_position] - change position",
        "fp/[name]  - find position",
        "dp/[name]  - delete position",
        "ab/[name]/[date]  - add birthday",
        "fb/[name]  - find birthday",
        "ga/[name]  - get age",
        "de/[name]  - delete employee",
        "all-info - show all info",
        "all-b - show all birthdays",
        "all-b-c - show all birthdays on the current week",
        "commands  - display all commands",
        "close  - close the program",
        "exit  - exit the program",
    ]

    formatted_commands = align_commands(commands_list)

    print(f"{Fore.LIGHTBLUE_EX}BOOK STAFF{Fore.RESET}")

    while True:
        try:
            user_input = input(f"{Fore.LIGHTGREEN_EX}Enter a command: {Fore.RESET}")
            command, *args = parse_input(user_input)

            if command == "close":
                print(f"{Fore.LIGHTYELLOW_EX}good bye{Fore.RESET}")
                save_data(book)
                break

            elif command == "exit":
                print(f"{Fore.LIGHTYELLOW_EX}have a nice day{Fore.RESET}")
                save_data(book)
                break

            elif command == "all-info":
                book.show_all()

            elif command == "all-b":
                book.show_all_birthdays()

            elif command == "all-c-b":
                book.show_coming_birthdays()

            elif command in methods:
                print(
                    f"{Fore.LIGHTBLUE_EX}{(methods[command])(args, book)}{Fore.RESET}"
                )

            elif command == "commands":
                print(f"{Fore.MAGENTA}{formatted_commands}{Fore.RESET}")

            else:
                print(f"{Fore.LIGHTRED_EX}invalid command{Fore.RESET}")

        except ValueError as e:
            print(f"{Fore.LIGHTRED_EX}{e}{Fore.RESET}")
            continue


if __name__ == "__main__":
    main()

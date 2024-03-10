import pickle

from colorama import Fore

from classes import Employee, Staff
from functions import parse_input, table_output


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
        "cb": Employee.edit_birthday,
        "db": Employee.remove_birthday,
        "fb": Employee.find_birthday,
        "ga": Employee.get_age,
        "de": Employee.remove_employee,
    }

    commands_list = [
        "commands - display all commands",
        "ap/[name]/[position] - add position",
        "cp/[name]/[old_position]/[new_position] - change position",
        "fp/[name](format: name surname ) - find position",
        "dp/[name]/[position] - delete position",
        "ab/[name]/[date](format: 09.09.1999) - add birthday",
        "fb/[name] - find birthday",
        "cb/[name]/[date] - change birthday",
        "db/[name] - delete birthday",
        "ga/[name] - get age",
        "de/[name] - delete employee",
        "all-info - show all info",
        "all-b - show all birthdays",
        "all-b-c - show all birthdays on the current week",
        "close - close the program",
        "exit - exit the program",
    ]

    formatted_commands = table_output(commands_list, "commands")

    print(f"{Fore.LIGHTBLUE_EX}BOOK STAFF{Fore.RESET}")

    while True:
        try:
            user_input = input(f"{Fore.LIGHTGREEN_EX}Enter a command: {Fore.RESET}")
            command, *args = parse_input(user_input)

            if command == "close":
                print(f"{Fore.GREEN}good bye{Fore.RESET}")
                save_data(book)
                break

            elif command == "exit":
                print(f"{Fore.GREEN}have a nice day{Fore.RESET}")
                save_data(book)
                break

            elif command == "all-info":
                book.show_all()

            elif command == "all-b":
                book.show_all_birthdays()

            elif command == "all-b-c":
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

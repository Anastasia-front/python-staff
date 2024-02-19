from classes import Employee, Staff
from functions import parse_input


def main():
    book = Staff()
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

    commands = [
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
        "all-b-c - show all birthdays on current week",
        "commands  - display all commands",
        "close  - close the program",
        "exit  - exit the program",
    ]

    print("Book staff")

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command == "close":
                print("Good bye")
                break

            elif command == "exit":
                print("Have a nice day")
                break

            elif command == "all-info":
                book.show_all()

            elif command == "all-b":
                book.show_all_birthdays()

            elif command == "all-c-b":
                book.show_coming_birthdays()

            elif command in methods:
                print((methods[command])(args, book))

            elif command == "commands":
                for cmd in commands:
                    print(cmd)

            else:
                print("Invalid command.")

        except ValueError as e:
            print(e)
            continue  # Continue to the next iteration of the loop


if __name__ == "__main__":
    main()

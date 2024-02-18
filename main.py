from classes import Record, Staff
from functions import parse_input


def main():
    book = Staff()
    methods = {
        "ap": Record.add_position,  # add position
        "cp": Record.edit_position,  # change position
        "fp": Record.find_position,  # find position
        "dp": Record.remove_position,  # delete position
        "ab": Record.add_birthday,  # add birthday
        "fb": Record.find_birthday,  # find birthday
        "de": Record.remove_employee,  # delete employee
        # "all-b": Record.birthdays,  # all birthdays
        # "all-info": Staff.show_all,  # all info
    }

    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "all-info":
                book.show_all()

            elif command == "all-b":
                book.show_all_birthdays()

            elif command in methods:
                print((methods[command])(args, book))

            else:
                print("Invalid command.")

        except ValueError as e:
            print(e)
            continue  # Continue to the next iteration of the loop


if __name__ == "__main__":
    main()

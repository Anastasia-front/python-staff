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
        "all-b": Record.birthdays,  # all birthdays
        # "all-info": Staff.show_all,  # all info
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "all-info":
            book.show_all()

        elif command in methods:
            try:
                print((methods[command])(args, book))
            except ValueError as e:
                print(e)
        # elif command == "add":
        #     print(methods["add"](args, book))

        # elif command == "change":
        #     print(methods["change"](args, book))

        # elif command == "position":
        #     print(methods["position"](args, book))

        # elif command == "delete-position":
        #     print(methods["delete-position"](args, book))

        # elif command == "all":
        #     for name, record in book.data.items():
        #         print(record)

        # elif command == "add-birthday":
        #     print(methods["add-birthday"](args, book))

        # elif command == "show-birthday":
        #     print(methods["show-birthday"](args, book))

        # elif command == "birthdays":
        #     print(methods["birthdays"](args, book))

        # elif command == "delete-employee":
        #     print(methods["delete-employee"](args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

from datetime import datetime

from functions import get_upcoming_birthdays

from .birthday import Birthday
from .name import Name
from .position import Position


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.positions = []
        self.birthday = None

    @classmethod
    def add_position(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and position for the employee"

        name, position = args

        if Position(position) and Name(name):
            exist = book.find( Name(name))
            if not exist:
                record = cls(name)
                record.positions.append(Position(position))
                book.add_record(record)
                return "position added"
            else:
                exist.positions.append(Position(position))
                return "position added"
        else:
            return "invalid name or position"
    
    @classmethod
    def add_birthday(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and date for the birthday"

        name, date = args

        try:
            datetime.strptime(date, "%d.%m.%Y")
            exist = book.find(name.capitilize())
            if not exist:
                return "employee not found"
            else:
                exist.birthday = Birthday(date)
                return "Birthday added"
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY"

    @classmethod
    def remove_position(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and position of the employee"

        name, position = args

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            exist.positions = [p for p in exist.positions if p.value != position]
            return "position deleted"

    @classmethod
    def remove_birthday(cls, args: list, book):
        if len(args) < 2:
            return "provide name of the employee"

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            exist.birthday = None
            return "Birthday deleted"

    @classmethod
    def remove_employee(cls, args: list, book):
        if len(args) < 1:
            return "provide name of the employee"

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            book.delete(name)
            return "employee deleted"

    @classmethod
    def edit_position(cls, args: list, book):
        if len(args) < 3:
            return "provide all arguments name,old and new positions of the employee"

        name, old_position, new_position = args

        if (not old_position.isdigit() or len(old_position) != 10) or (
            not new_position.isdigit() or len(new_position) != 10
        ):
            return "position number must consist of 10 digits"

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            for position in exist.positions:
                if position.value == old_position:
                    position.value = new_position
                    return "position changed"
        return "position not found"

    @classmethod
    def edit_birthday(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and date for the birthday"

        name, date = args

        try:
            datetime.strptime(date, "%d.%m.%Y")
            exist = book.find(name)
            if not exist:
                return "employee not found"
            else:
                exist.birthday = Birthday(date)
                return "Birthday changed"
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY"

    @classmethod
    def find_position(cls, args: list, book) -> Position:

        if len(args) < 1:
            return "provide name of the employee"

        employee = args[0]

        for name, record in book.data.items():
            if name == employee:
                return record
            else:
                continue
        return "employee not found"

    @classmethod
    def find_birthday(cls, args: list, book) -> Birthday:

        if len(args) < 1:
            return "provide name of the employee"

        employee = args[0]

        for name, record in book.data.items():
            if employee == name:
                return record.birthday
            else:
                continue
        return "employee not found"

    @classmethod
    def birthdays(cls, args: list, book) -> Birthday:
        get_upcoming_birthdays(book)

    def __str__(self):

        birthday_info = ""
        if self.birthday:
            birthday_info = f"Birthday date: {self.birthday.value.strftime('%d %B %Y')}"

        positions_info = ", ".join(str(p) for p in self.positions)

        return f"      - Name: {self.name.value} | Position: {positions_info} |  {birthday_info}"

from datetime import datetime

from .birthday import Birthday
from .name import Name
from .position import Position

current_datetime = datetime.now()
current_year = current_datetime.year


class Employee:
    def __init__(self, name: str):
        self.name = Name(name)
        self.positions = []
        self.birthday = None
        self.age = None

    def calculate_age(self):
        if self.birthday:
            birth_date = self.birthday.value
            current_date = datetime.now()

            age_delta = current_date - birth_date
            years = age_delta.days // 365

            self.age = years
            return years
        else:
            return None

    @classmethod
    def get_age(cls, args: list, book):
        if len(args) < 1:
            return "provide name of the employee"

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            if exist.birthday:
                return f"{exist.name} is {exist.calculate_age()} y.o"
            else:
                return f"there is no information about {exist.name}'s birthday"

    @classmethod
    def add_position(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and position for the employee"

        name, position = args

        exist = book.find(name)
        if not exist:
            record = cls(name)
            record.positions.append(Position(position))
            book.add_record(record)
            return "position added"
        else:
            exist.positions.append(Position(position))
            return "position added"

    @classmethod
    def add_birthday(cls, args: list, book):
        if len(args) < 2:
            return "provide both name and date for the birthday"

        name, date = args
        try:
            datetime.strptime(date, "%d.%m.%Y")
            exist = book.find(name)
            if not exist:
                return "employee not found"
            elif exist.birthday:
                return "employee has already had birthday info"
            else:
                exist.birthday = Birthday(date)
                exist.calculate_age()
                return "birthday added"
        except ValueError:
            return "invalid date format. Use DD.MM.YYYY"

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
        if len(args) < 1:
            return "provide name of the employee"

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "employee not found"
        else:
            exist.birthday = None
            exist.age = None
            return "birthday deleted"

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
                exist.calculate_age()
                return "birthday changed"
        except ValueError:
            return "invalid date format. Use DD.MM.YYYY"

    @classmethod
    def find_position(cls, args: list, book) -> Position:

        if len(args) < 1:
            return "provide name of the employee"

        employee = args[0]

        for name, record in book.data.items():
            if name == employee:
                positions_values = [position.value for position in record.positions]
                return (
                    ", ".join(positions_values)
                    if positions_values
                    else "employee has no info about position"
                )
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
                if record.birthday:
                    return record.birthday
                else:
                    return "employee has no info about birthday"
            else:
                continue
        return "employee not found"

    def __str__(self):
        birthday_info = (
            self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "no info"
        )

        age = f"{self.age} y.o." if self.age else "no info"

        positions_info = ", ".join(str(p) for p in self.positions)

        return f"{self.name} - {positions_info} -  {birthday_info} - {age}"

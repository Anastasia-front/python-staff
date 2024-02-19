from collections import UserDict

from functions import coming_birthdays

from .employee import Employee


class Staff(UserDict):
    def add_record(self, record: Employee):
        self.data[record.name.value] = record

    def find(self, name: str) -> Employee:
        return self.data.get(name)

    def show_all(self):
        for name, record in self.data.items():
            print(record)

    def show_all_birthdays(self):
        for name, record in self.data.items():
            print(f" - Name: {name} | Birthday date: {record.birthday}")

    def show_coming_birthdays(self):
        coming_birthdays(self)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

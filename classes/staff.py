from collections import UserDict

from .record import Record


class Staff(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def show_all(self):
        for name, record in self.data.items():
            print(record)

    def show_all_birthdays(self):
        for name, record in self.data.items():
            print(record.birthday)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

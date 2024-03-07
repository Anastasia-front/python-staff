from collections import UserDict

from colorama import Fore

from functions import coming_birthdays

from .employee import Employee


class Staff(UserDict):
    def add_record(self, record: Employee):
        self.data[record.name.value] = record

    def find(self, name: str) -> Employee:
        return self.data.get(name)

    def show_all(self):
        for name, record in self.data.items():
            print(f"{Fore.LIGHTCYAN_EX}{record}{Fore.RESET}")

    def show_all_birthdays(self):
        for name, record in self.data.items():
            print(
                f"{Fore.CYAN} - Name: {name} | Birthday date: {record.birthday}{Fore.RESET}"
            )

    def show_coming_birthdays(self):
        coming_birthdays(self)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

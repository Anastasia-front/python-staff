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
        if len(self.data.items()) != 0:
            for name, record in self.data.items():

                print(f"{Fore.LIGHTCYAN_EX}{record}{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}no information yet{Fore.RESET}")

    def show_all_birthdays(self):
        if len(self.data.items()) != 0:
            for name, record in self.data.items():
                print(
                    f"{Fore.CYAN} - name: {name} | birthday date: {record.birthday}{Fore.RESET}"
                )
        else:
            print(f"{Fore.CYAN}no information yet{Fore.RESET}")

    def show_coming_birthdays(self):
        coming_birthdays(self)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

from datetime import datetime, timedelta

from colorama import Fore

from .table_output import table_output

current_datetime = datetime.now()
current_year = current_datetime.year


def coming_birthdays(book):
    upcoming_birthdays = []

    if not book:
        print(f"{Fore.LIGHTWHITE_EX}no birthdays{Fore.RESET}")

    for name, employee in book.items():
        date = employee.birthday

        if not date:
            print(f"no information about birthday of {employee.name}", end="")
        else:
            datetime_object = datetime.strptime(str(date), "%d.%m.%Y")
            day = datetime_object.weekday()

            if day == 6:
                day_interval = timedelta(days=2)
                datetime_object = datetime_object + day_interval
            elif day == 7:
                day_interval = timedelta(days=1)
                datetime_object = datetime_object + day_interval

            target_day = datetime_object.day

            # days_until_birthday = (datetime_object - current_datetime).days

            # if 0 <= days_until_birthday <= 7:
            date = date.value.replace(year=current_year, day=target_day)
            date = date.strftime("%A, %d of %B")
            upcoming_birthdays.append(
                f"{employee.name.value} - {employee.birthday} - {date} - {employee.age} y.o."
            )

    if len(upcoming_birthdays) != 0:
        print(table_output(upcoming_birthdays, "coming_birthdays"))
    else:
        print(
            f"{Fore.LIGHTWHITE_EX}there is no one birthday on current week{Fore.RESET}"
        )

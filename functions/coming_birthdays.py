from datetime import datetime, timedelta

current_datetime = datetime.now()
current_year = current_datetime.year


def coming_birthdays(book):
    upcoming_birthdays = []

    if not book:
        print("no birthdays")

    for name, employee in book.items():
        date = employee.birthday

        if not date:
            continue
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

            # Calculate the number of days until the next birthday
            days_until_birthday = (datetime_object - current_datetime).days

            # Check if the birthday is within the next week
            if 0 <= days_until_birthday <= 7:
                date = str(current_year) + date[4:8] + str(target_day)

            employee.congratulation_date = date
            upcoming_birthdays.append(employee)

        message = "List for congratulations on the current week:\n"
        employee.age = employee.calculate_age()

        for employee in upcoming_birthdays:
            birthday_date = employee.congratulation_date
            formatted_birthday = datetime.strptime(
                str(birthday_date), "%d.%m.%Y"
            ).strftime("%d of %B")
            message += f"{formatted_birthday} - {employee.name}, {employee.age} years, will have a birthday on {datetime_object.strftime('%A')}\n"

        print(message, end="")

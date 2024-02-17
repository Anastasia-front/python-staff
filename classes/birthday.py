from datetime import datetime

from .field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError as e:
            raise ValueError("Invalid date format. Use DD.MM.YYYY.") from e

    def __str__(self):
        return f"{self.value.strftime('%d %B %Y')}"

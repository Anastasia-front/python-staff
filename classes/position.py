from .field import Field


class Position(Field):
    def __init__(self, value):
        try:
            if not value.isalpha():
                raise ValueError("position must consist of letters")
            else:
                super().__init__(value)

        except ValueError:
            raise ValueError("position must consist of letters")

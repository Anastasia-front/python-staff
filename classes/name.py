from .field import Field


class Name(Field):
    def __init__(self, value):
        parts = value.split()
        if " " not in value:
            raise ValueError(
                "name must consist of name and surname and split by space (example: name surname)"
            )
        elif not all(part.isalpha() for part in parts):
            raise ValueError("name and surname must contain only letters")
        else:
            super().__init__(value.lower())

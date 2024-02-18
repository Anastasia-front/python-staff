from .field import Field


class Name(Field):
    def __init__(self, value):
        try:
            if " " not in value:
                raise ValueError(
                    "name must consist of name and surname and split by space (example: name surname)"
                )
            else:
                super().__init__(value.lower())

        except ValueError:
            raise ValueError(
                "name must consist of name and surname and split by space (example: name surname)"
            )

from .field import Field


class Name(Field):
    def __init__(self, value):
        try:
            if not value.find("_").isalpha():
                raise ValueError(
                    "name must consist of name and surname and split by underscore (example: name_surname)"
                )

            # Capitalize the first letter of each word
            capitalized_name = " ".join(word.capitalize() for word in value.split())

            super().__init__(capitalized_name)
        except ValueError as e:
            print(e)

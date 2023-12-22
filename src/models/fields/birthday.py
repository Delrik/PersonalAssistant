from .field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, birthday):
        self.validate_birthday(birthday)
        super().__init__(birthday)

    @staticmethod
    def validate_birthday(birthday):
        try:
            datetime.strptime(birthday, '%d.%m.%Y')
        except ValueError:
            raise ValueError(f"{birthday} is not a valid birthday. Use the format 'DD.MM.YYYY'.")

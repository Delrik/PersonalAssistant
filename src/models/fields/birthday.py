from .field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, birthday):
        self.validate_birthday(birthday)
        super().__init__(birthday)

    @staticmethod
    def validate_birthday(birthday):
        if not Birthday.is_valid(birthday):
            raise ValueError(f"{birthday} is not a valid birthday.")

    @staticmethod
    def is_valid(birthday):
        try:
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
            if birthday_date.date() > datetime.now().date():
                return False
        except ValueError:
            return False
        return True

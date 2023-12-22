from .field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, birthday):
        self.validate_birthday(birthday)
        super().__init__(birthday)

    @staticmethod
    def validate_birthday(birthday):
        try:
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y")

            # Check if the birthday is later than today's date
            if birthday_date.date() > datetime.now().date():
                raise ValueError(f"{birthday} is not a valid birthday.")
        except ValueError:
            raise ValueError(f"{birthday} is not a valid birthday.")

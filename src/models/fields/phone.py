from .field import Field


class Phone(Field):
    def __init__(self, phone):
        self.validate_phone(phone)
        super().__init__(phone)

    @staticmethod
    def validate_phone(phone):
        if not Phone.is_valid(phone):
            raise ValueError(f"{phone} is not a valid phone number.")

    @staticmethod
    def is_valid(phone):
        if len(phone) != 10:
            return False
        if not phone.isnumeric():
            return False
        return True

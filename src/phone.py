from field import Field


class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError(f"{phone} is invalid, it should be 10 digits length")
        elif not phone.isnumeric():
            raise ValueError(f"{phone} is invalid, it should consist only of numbers")
        super().__init__(phone)

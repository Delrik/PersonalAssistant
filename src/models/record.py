from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            raise KeyError(
                f"The phone number '{phone}' already exists.")
        self.phones.append(phone)

    def set_address(self, address):
        self.address = Address(address)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {self.phones}"

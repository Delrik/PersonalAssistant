from .fields.birthday import Birthday
from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.birthday = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def set_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_birthday(self):
        self.birthday = None

    def change_birthday(self, new_birthday):
        self.add_birthday(new_birthday)



    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}"

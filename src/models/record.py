from .fields.email import Email
from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.email = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def set_address(self, address):
        self.address = Address(address)

    def add_email(self, email):
        self.email = Email(email)

    def remove_email(self):
        self.email = None

    def change_email(self, new_email):
        self.add_email(new_email)

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}, email: {self.email}"

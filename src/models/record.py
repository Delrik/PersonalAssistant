from .fields.phone import Phone
from .fields.name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}"

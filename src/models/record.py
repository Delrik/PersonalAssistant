from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address
from .fields.note import Note


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.note = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def set_address(self, address):
        self.address = Address(address)

    def add_note(self, title, note):
        self.note = Note(title, note)

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}, note: {self.note}"

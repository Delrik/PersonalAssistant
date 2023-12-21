from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if str(phone) in [str(p) for p in self.phones]:
            raise KeyError(
                f"The phone number {phone} already exists.")
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)

    def change_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone.value) == old_phone:
                self.phones[index] = Phone(new_phone)
                return
        raise KeyError(
                f"{phone} not found, add correct number please.")

    def set_address(self, address):
        self.address = Address(address)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {self.phones}"

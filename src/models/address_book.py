from collections import UserDict
import pickle
from .record import Record


class AddressBook(UserDict):
    def add_record(self, name, phone):
        if name in self.data:
            raise KeyError(f"The contact with this name '{name}' already exists.")
        record = Record(name)
        record.add_phone(phone)
        self.data[name] = record

    def set_address(self, name, address):
        record = self.find(name)
        record.set_address(address)

    def add_note(self, name, title, text):
        record = self.find(name)
        record.add_note(title, text)

    def remove_note(self, name, title):
        record = self.find(name)
        record.remove_note(title)

    def find(self, name) -> Record:
        if not name in self.data:
            raise KeyError(f"The contact with this name '{name}' does not exist.")
        return self.data[name]

    def findAll(self):
        if len(self.data) == 0:
            raise KeyError(f"The contact list is empty.")
        return [
            f"{name}: {self.data[name].phone}, note: {self.data[name].notes}"
            for name in self.data.keys()
        ]

    def save_to_file(self):
        with open("db.bin", "wb") as file:
            pickle.dump(self, file)

    def read_from_file():
        try:
            with open("db.bin", "rb") as file:
                return pickle.load(file)
        except:
            return None

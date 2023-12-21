from collections import UserDict
import pickle
from .record import Record


class AddressBook(UserDict):
    def add_record(self, name, phone):
        if name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' already exists.")
        record = Record(name)
        record.add_phone(phone)
        self.data[name] = record

    def set_address(self, name, address):
        record = self.find(name)
        record.set_address(address)

    def find(self, name) -> Record:
        if not name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' does not exist.")
        return self.data[name]

    def save_to_file(self):
        with open("db.bin", "wb") as file:
            pickle.dump(self, file)

    def read_from_file():
        try:
            with open("db.bin", "rb") as file:
                return pickle.load(file)
        except:
            return None

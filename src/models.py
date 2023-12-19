from collections import UserDict
import pickle


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError(f"{phone} is invalid, it should be 10 digits length")
        elif not phone.isnumeric():
            raise ValueError(f"{phone} is invalid, it should consist only of numbers")
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}"


class AddressBook(UserDict):
    def add_record(self, name, phone):
        if name in self.data:
            raise KeyError(f"The contact with this name '{name}' already exists.")
        record = Record(name)
        record.add_phone(phone)
        self.data[name] = record

    def find(self, name):
        if not name in self.data:
            raise KeyError(f"The contact with this name '{name}' does not exist.")
        return self.data[name]

    def findAll(self):
        if len(self.data) == 0:
            raise KeyError(f"The contact list is empty.")
        return [f"{name}: {self.data[name].phone}" for name in self.data.keys()]

    def save_to_file(self):
        with open("db.bin", "wb") as file:
            pickle.dump(self, file)

    def read_from_file():
        try:
            with open("db.bin", "rb") as file:
                return pickle.load(file)
        except:
            return None

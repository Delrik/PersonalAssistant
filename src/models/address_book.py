from collections import UserDict
import pickle
from .record import Record


class AddressBook(UserDict):
    def add_record(self, name):
        if name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' already exists.")
        record = Record(name)
        self.data[name] = record

    def find(self, name) -> Record:
        if not name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' does not exist.")
        return self.data[name]

    def findNotesByTag(self, tag):
        result = []

        for name in self.data:
            for note in self.data[name].notes:
                if tag.lower() in note.tags:
                    result.append((name, note))

        if len(result) == 0:
            raise KeyError(f"No notes found.")

        return result

    def save_to_file(self):
        with open("db.bin", "wb") as file:
            pickle.dump(self, file)

    def read_from_file():
        try:
            with open("db.bin", "rb") as file:
                return pickle.load(file)
        except:
            return None

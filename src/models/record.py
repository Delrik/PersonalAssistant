from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address
from .fields.note import Note


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.notes = []

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def set_address(self, address):
        self.address = Address(address)

    def add_note(self, title, text):
        note = self.findNoteByTitle(title)
        if note != None:
            raise KeyError(f"The note with this title '{title}' already exists.")
        self.notes.append(Note(title, text))

    def remove_note(self, title):
        note = self.findNoteByTitle(title)
        if note == None:
            raise KeyError(f"The note with this title '{title}' does not exist.")
        self.notes = list(filter(lambda note: note.title != title, self.notes))

    def findNoteByTitle(self, title):
        note = list(filter(lambda note: note.title == title, self.notes))
        return None if len(note) == 0 else note[0]

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}, notes: {self.notes}"

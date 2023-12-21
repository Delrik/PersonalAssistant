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
        note_index = self.findNoteIndexByTitle(title)
        if note_index > -1:
            raise KeyError(f"The note with this title '{title}' already exists.")
        self.notes.append(Note(title, text))

    def remove_note(self, title):
        self.check_note_availability(title)
        self.notes = list(filter(lambda note: note.title != title, self.notes))

    def change_note(self, title, new_text):
        note_index = self.check_note_availability(title)
        self.notes[note_index].text = new_text

    def change_note_title(self, title, new_title):
        note_index = self.check_note_availability(title)
        self.notes[note_index].title = new_title

    def check_note_availability(self, title):
        note_index = self.find_note_index_by_title(title)
        if note_index == -1:
            raise KeyError(f"The note with this title '{title}' does not exist.")
        return note_index

    def find_note_index_by_title(self, title):
        index = -1
        for i, note in enumerate(self.notes):
            if note.title == title:
                index = i
                break
        return index

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}, notes: {self.notes}"

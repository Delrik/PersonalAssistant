from .fields.birthday import Birthday
from .fields.email import Email
from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address
from .fields.note import Note


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.notes = []
        self.email = None
        self.birthday = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def set_address(self, address):
        self.address = Address(address)

    def add_note(self, title, text):
        self.notes.append(Note(title, text))

    def find_note(self, title):
        note_index = self.find_note_index_by_title(title)
        if note_index == -1:
            raise KeyError(f"The note with this title '{title}' does not exist.")
        return self.notes[note_index]

    def remove_note(self, title):
        self.notes = list(
            filter(lambda note: note.title.lower() != title.lower(), self.notes)
        )

    def change_note(self, title, new_text):
        self.find_note(title).text = new_text

    def change_note_title(self, title, new_title):
        self.find_note(title).title = new_title

    def add_tag(self, title, tag):
        self.find_note(title).add_tag(tag)

    def find_note_index_by_title(self, title):
        index = -1
        for i, note in enumerate(self.notes):
            if note.title.lower() == title.lower():
                index = i
                break
        return index

    def is_note_exist(self, title):
        note_index = self.find_note_index_by_title(title)
        return note_index > -1

    def set_email(self, email):
        self.email = Email(email)

    def remove_email(self):
        self.email = None

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_birthday(self):
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name}, phone: {self.phone}, email: {self.email}, birthday: {self.birthday}, notes: {self.notes}"

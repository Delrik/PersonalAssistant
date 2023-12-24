from .fields.birthday import Birthday
from .fields.email import Email
from .fields.phone import Phone
from .fields.name import Name
from .fields.address import Address
from .fields.note import Note
from rich.text import Text


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.notes = []
        self.email = None
        self.birthday = None

    def add_phone(self, phone):
        phone = Phone(phone)
        if str(phone) in [str(p) for p in self.phones]:
            raise KeyError(f"Phone number {phone} already exists.")
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone.value) == old_phone:
                self.phones[index] = Phone(new_phone)
                return
        raise KeyError(f"{old_phone} not found, add correct number please.")

    def remove_phone(self, phone):
        if str(phone) in [str(p) for p in self.phones]:
            self.phones = [
                existing_phone
                for existing_phone in self.phones
                if existing_phone.value != phone
            ]
        else:
            raise KeyError(f"{phone} not found, add correct number please.")

    def set_address(self, address):
        self.address = Address(address)

    def remove_address(self):
        self.address = None

    def add_note(self, title, text):
        if self.is_note_exist(title):
            raise KeyError(
                f"The note with this title '{title}' already exists.")
        self.notes.append(Note(title, text))

    def find_note(self, title):
        note_index = self.find_note_index_by_title(title)
        if note_index == -1:
            raise KeyError(
                f"The note with this title '{title}' does not exist.")
        return self.notes[note_index]

    def remove_note(self, title):
        self.notes = list(
            filter(lambda note: note.title.lower()
                   != title.lower(), self.notes)
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

    def __rich__(self):
        formatted_contact = Text()
        formatted_contact.append("Contact name: ", style="yellow")
        formatted_contact.append(f"{self.name}\n", style="bold blue")

        if self.phones:
            phone_list = ", ".join(str(phone) for phone in self.phones)
            formatted_contact.append("Phones: ", style="yellow")
            formatted_contact.append(f"{phone_list}\n", style="blue")

        if self.address and self.address.value:
            formatted_contact.append("Address: ", style="yellow")
            formatted_contact.append(f"{self.address}\n", style="blue")

        if self.email and self.email.value:
            formatted_contact.append("Email: ", style="yellow")
            formatted_contact.append(f"{self.email}\n", style="blue")

        if self.birthday and self.birthday.value:
            formatted_contact.append("Birthday: ", style="yellow")
            formatted_contact.append(f"{self.birthday}\n", style="blue")

        if self.notes:
            notes_text = Text()
            for note in self.notes:
                notes_text.append(f"{note.title}: ", style="bold blue")
                notes_text.append(f"{note.text} ", style="blue")
                if note.tags:
                    formatted_tags = ", ".join(note.tags)
                    notes_text.append(formatted_tags, style="green")
                notes_text.append("\n")

            formatted_contact.append(f"Notes:\n", style="yellow")
            formatted_contact.append(notes_text)

        return formatted_contact

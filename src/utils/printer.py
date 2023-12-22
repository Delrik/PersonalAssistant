class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Printer(metaclass=SingletonMeta):
    def welcome(self):
        print("Welcome to your Personal Assistant!")

    def print_hello(self):
        print("How can I help you?")

    def print_exit(self):
        print("Good bye!")

    def print_invalid_command(self):
        print("Invalid command.")

    def print_is_already_exist(self, value):
        print(f"The '{value}' is already exists.")

    def print_is_not_exist(self, value):
        print(f"The '{value}' is not exists.")

    def print_contact(self, contact):
        print(contact)

    def print_all_contacts(self, book):
        for record in book.data.values():
            self.print_contact(record)

    def print_error(self, error):
        print(error)

    def print_contact_added(self, contact):
        print(f"The contact added.\n {contact}")

    def print_contact_deleted(self, name):
        print(f"The contact '{name}' deleted.")

    def print_contact_changed(self, contact):
        print(f"The contact changed.\n {contact}")

    def print_address_changed(self, contact):
        print(f"The address changed.\n {contact}")

    def print_phone_changed(self, contact):
        print(f"The phone changed.\n {contact}")

    def print_email_changed(self, contact):
        print(f"The email changed.\n {contact}")

    def print_note_added(self, record):
        print(f"The note added.\n {record}")

    def print_note_removed(self, title):
        print(f"The note removed.\n {title}")

    def print_note_changed(self, record):
        print(f"The note changed.\n {record}")

    def print_note_found(self, note):
        print(f"The note found.\n {note}")

    def print_notes_found(self, notes):
        for note in notes:
            self.print_note_found(note)

    def print_tag_added(self, record, title, tag):
        print(f"The tag added.\n {record}")

    def print_email_added(self, record):
        print(f"The email added.\n {record}")

    def print_email_removed(self, record):
        print(f"The email removed.\n {record}")

    def print_email_changed(self, record):
        print(f"The email changed.\n {record}")

    def print_birthday_added(self, record):
        print(f"The birthday added.\n {record}")

    def print_birthday_removed(self, record):
        print(f"The birthday removed.\n {record}")

    def print_birthday_changed(self, record):
        print(f"The birthday changed.\n {record}")

    def print_birthday_found(self, record):
        print(f"The birthday found.\n {record}")

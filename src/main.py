from models.address_book import AddressBook
from models.printer import Printer
from models.completer import CommandCompleter
from prompt_toolkit import PromptSession


def handle_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            Printer().print_error(e)

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@handle_error
def add_contact(args, book):
    if len(args) == 0:
        raise IndexError("Enter name and phone number")
    if len(args) == 1:
        raise IndexError("Enter phone number")
    name, phone = args
    book.add_record(name, phone)
    # TODO: Print
    return "Contact added."


@handle_error
def change_contact(args, book):
    if len(args) == 0:
        raise IndexError("Enter name and phone number")
    if len(args) == 1:
        raise IndexError("Enter phone number")
    name, phone = args
    book.find(name).add_phone(phone)
    # TODO: Print
    return "Contact changed."


@handle_error
def get_contact_phone(args, book):
    if len(args) == 0:
        raise IndexError("Enter name")
    name = args[0]
    # TODO: Print
    return book.find(name).phone


@handle_error
def get_all_contacts(book):
    Printer().print_all_contacts(book)


@handle_error
def add_email(args, book):
    if len(args) < 2:
        raise IndexError("Enter name and email")

    name, email = args
    contact = book.find(name)
    contact.set_email(email)

    # TODO: Print
    return f"Email added for {name}."


@handle_error
def remove_email(args, book):
    if len(args) == 0:
        raise IndexError("Enter name")

    name = args[0]
    contact = book.find(name)
    contact.remove_email()

    # TODO: Print
    return f"Email removed for {name}."


@handle_error
def change_email(args, book):
    if len(args) < 2:
        raise IndexError("Enter name and new email")

    name, new_email = args
    contact = book.find(name)
    contact.set_email(new_email)

    # TODO: Print
    return f"Email changed for {name}."


@handle_error
def add_birthday(args, book):
    if len(args) < 2:
        raise IndexError("Enter name and birthday")

    name, birthday = args
    contact = book.find(name)
    contact.set_birthday(birthday)

    # TODO: Print
    return f"Birthday added for {namse}."


@handle_error
def remove_birthday(args, book):
    if len(args) == 0:
        raise IndexError("Enter name")

    name = args[0]
    contact = book.find(name)
    contact.remove_birthday()

    # TODO: Print
    return f"Birthday removed for {name}."


@handle_error
def change_birthday(args, book):
    if len(args) < 2:
        raise IndexError("Enter name and new birthday")

    name, new_birthday = args
    contact = book.find(name)
    contact.set_birthday(new_birthday)

    # TODO: Print
    return f"Birthday changed for {name}."


def main():
    book = (
        AddressBook.read_from_file()
        if AddressBook.read_from_file() != None
        else AddressBook()
    )

    Printer().welcome()

    session = PromptSession(completer=CommandCompleter())
    while True:
        user_input = session.prompt("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save_to_file()
            Printer().print_exit()
            break
        elif command == "hello":
            Printer().print_hello()
        elif command == "add":
            add_contact(args, book)
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_contact_phone(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "remove-email":
            print(remove_email(args, book))
        elif command == "change-email":
            print(change_email(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "remove-birthday":
            print(remove_birthday(args, book))
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "birthdays":
            print()
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()
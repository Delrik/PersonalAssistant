from models.address_book import AddressBook
from models.printer import Printer
from utils.completer import get_command_completer
from prompt_toolkit import PromptSession


def handle_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except KeyError as e:
            return e
        except IndexError as e:
            return e

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
    # TODO: Print
    return book.findAll()


def main():
    book = (
        AddressBook.read_from_file()
        if AddressBook.read_from_file() != None
        else AddressBook()
    )

    Printer().welcome()

    session = PromptSession(completer=get_command_completer())
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
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()

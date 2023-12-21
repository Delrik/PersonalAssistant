from models.address_book import AddressBook
from models.printer import Printer


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


@handle_error
def add_birthday(args, book):
    if len(args) < 2:
        raise IndexError("Enter name and birthday")

    name, birthday = args
    contact = book.find(name)
    contact.add_birthday(birthday)

    # TODO: Print
    return f"Birthday added for {name}."


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
    contact.change_birthday(new_birthday)

    # TODO: Print
    return f"Birthday changed for {name}."


def main():
    book = (
        AddressBook.read_from_file()
        if AddressBook.read_from_file() != None
        else AddressBook()
    )

    Printer().welcome()

    while True:
        user_input = input("Enter a command: ")
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
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "remove-birthday":
            print(remove_birthday(args, book))
        elif command == "change-birthday":
            print(change_birthday(args, book))
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()

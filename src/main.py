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


@handle_error
def parse_input(user_input, lower=False):
    cmd, *args = user_input.split()
    cmd = cmd.strip()
    if lower:
        cmd = cmd.lower()
    return cmd, *args


def get_input_value(name, check_is_exist=None, type_check="not_exist"):
    while True:
        input_value = parse_input(input(f"Enter {name} (n-close): "))
        if type(input_value) == tuple:
            value = " ".join(input_value)
            if value == "n":
                break
            if check_is_exist:
                check_result = check_is_exist and check_is_exist(value)
                if type_check == "exist" and check_result:
                    Printer().print_is_already_exist(value)
                elif type_check == "not_exist" and not check_result:
                    Printer().print_is_not_exist(value)
                else:
                    return value
            else:
                return value


def get_name(args):
    name = " ".join(args)
    if len(name) == 0:
        raise IndexError("Enter contact name")
    return name


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
def add_note(args, book):
    name = get_name(args)
    record = book.find(name)
    title = get_input_value("title", record.is_note_exist, type_check="exist")
    if title != None:
        text = get_input_value("text")
        if text != None:
            record.add_note(title, text)
            return "Note added."
    return "Note creation is canceled."


@handle_error
def remove_note(args, book):
    name = get_name(args)
    record = book.find(name)
    title = get_input_value("title", record.is_note_exist)
    if title != None:
        record.remove_note(title)
        return "Note removed."
    return "Note removing is canceled."


@handle_error
def change_note(args, book):
    name = get_name(args)
    record = book.find(name)
    title = get_input_value("title", record.is_note_exist)
    if title != None:
        text = get_input_value("text")
        if text != None:
            record.change_note(title, text)
            return "Note changed."
    return "Note changing is canceled."


@handle_error
def change_note_title(args, book):
    name = get_name(args)
    record = book.find(name)
    old_title = get_input_value("old title", record.is_note_exist)
    if old_title != None:
        new_title = get_input_value("new title")
        if new_title != None:
            record.change_note_title(old_title, new_title)
            return "Note title changed."
    return "Note title changing is canceled."


@handle_error
def find_note(args, book):
    name = get_name(args)
    record = book.find(name)
    title = get_input_value("title", record.is_note_exist)
    if title != None:
        return record.find_note(title)
    return "Note searching is canceled."


@handle_error
def add_tag(args, book):
    name = get_name(args)
    record = book.find(name)
    title = get_input_value("title", record.is_note_exist)
    if title != None:
        note = record.find_note(title)
        tag = get_input_value("tag", note.is_exist, type_check="exist")
        if tag != None:
            record.add_tag(title, tag)
            return "Tag added."
    return "Tag adding is canceled."


@handle_error
def find_tag(args, book):
    if len(args) == 0:
        raise IndexError("Enter tag name")
    tag = args[0]
    return book.findNotesByTag(tag)


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
        command, *args = parse_input(user_input, lower=True)

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
        elif command == "add-note":
            print(add_note(args, book))
        elif command == "remove-note":
            print(remove_note(args, book))
        elif command == "change-note":
            print(change_note(args, book))
        elif command == "change-note-title":
            print(change_note_title(args, book))
        elif command == "find-note":
            print(find_note(args, book))
        elif command == "add-tag":
            print(add_tag(args, book))
        elif command == "find-tag":
            print(find_tag(args, book))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "remove-email":
            print(remove_email(args, book))
        elif command == "change-email":
            print(change_email(args, book))
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()

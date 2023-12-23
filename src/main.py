from collections import defaultdict
from models.address_book import AddressBook
from models.fields.birthday import Birthday
from models.fields.email import Email
from models.fields.phone import Phone
from utils.printer import Printer
from utils.completer import CommandCompleter
from prompt_toolkit import PromptSession, HTML
from datetime import timedelta, datetime
from utils.commands import command_descriptions


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


def get_name(args):
    name = " ".join(args)
    if len(name) == 0:
        raise IndexError("Enter contact name")
    return name


def get_day_of_week_from_date(input_date):
    return input_date.strftime("%A")


def is_empty_string(value):
    return value == ""


def get_valid_input(request, validity_func, error_msg):
    while True:
        value = Printer().get_styled_input(request)
        if validity_func(value):
            return value
        Printer().print_error(error_msg)


def get_any_input(request):
    return Printer().get_styled_input(request)


def get_contact_data(book, name):
    phone = get_valid_input(
        "Enter phone number (optional): ",
        lambda x: Phone.is_valid(x) or is_empty_string(x),
        "Invalid phone number (10 digits)",
    )
    if phone:
        book.find(name).add_phone(phone)

    birthday = get_valid_input(
        "Enter birthday (optional): ",
        lambda x: Birthday.is_valid(x) or is_empty_string(x),
        "Please enter a valid birthday in the format dd.mm.yyyy",
    )
    if birthday:
        book.find(name).set_birthday(birthday)

    address = get_any_input("Enter address (optional): ")
    book.find(name).set_address(address)

    email = get_valid_input(
        "Enter email (optional): ",
        lambda x: Email.is_valid(x) or is_empty_string(x),
        "Invalid email address",
    )
    if email:
        book.find(name).set_email(email)


@handle_error
def add_contact(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    book.add_record(name)
    get_contact_data(book, name)
    Printer().print_contact_added(book.find(name))


@handle_error
def find_contact(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    Printer().print_contact(contact)


@handle_error
def change_contact(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    book.find(name)
    get_contact_data(book, name)
    Printer().print_contact_changed(book.find(name))


@handle_error
def remove_contact(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    book.find(name)
    book.data.pop(name)
    Printer().print_contact_deleted(name)


@handle_error
def add_phone(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    phone = get_valid_input(
        "Enter phone number: ",
        lambda x: Phone.is_valid(x),
        "Invalid phone number(10 digits)",
    )
    record.add_phone(phone)
    Printer().print_phone_added(record)


@handle_error
def change_phone(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    old_phone = get_valid_input(
        "Enter old phone number: ",
        lambda x: Phone.is_valid(x),
        "Invalid phone number(10 digits)",
    )
    new_phone = get_valid_input(
        "Enter new phone number: ",
        lambda x: Phone.is_valid(x),
        "Invalid phone number(10 digits)",
    )
    record.change_phone(old_phone, new_phone)
    Printer().print_phone_changed(record)


@handle_error
def remove_phone(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    phone = get_valid_input(
        "Enter phone number to remove: ",
        lambda x: Phone.is_valid(x),
        "Invalid phone number(10 digits)",
    )
    record.remove_phone(phone)
    Printer().print_phone_removed(record)


@handle_error
def get_contact_phones(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)

    if record.phones:
        phone_numbers = [str(phone) for phone in record.phones]
        Printer().print_contact_phones(phone_numbers)
    else:
        Printer().print_error(f"No phone numbers found for '{name}'.")


@handle_error
def add_address(args, book):
    if len(args) == 0:
        raise (IndexError("Please enter a name."))
    name = " ".join(args)
    record = book.find(name)
    address = get_any_input("Enter address: ").strip()
    if len(address):
        record.set_address(address)
    Printer().print_address_added(record)


@handle_error
def change_address(args, book):
    if len(args) == 0:
        raise (IndexError("Please enter a name."))
    name = " ".join(args)
    record = book.find(name)
    address = get_any_input("Enter new address: ").strip()
    if len(address):
        record.set_address(address)
    Printer().print_address_changed(record)


@handle_error
def remove_address(args, book):
    if len(args) == 0:
        raise (IndexError("Please enter a name."))
    name = " ".join(args)
    record = book.find(name)
    record.remove_address()
    Printer().print_address_removed(record)


@handle_error
def get_all_contacts(book):
    Printer().print_all_contacts(book)


@handle_error
def add_note(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    if record.is_note_exist(title):
        raise KeyError(f"The note with this title '{title}' already exists.")
    note = get_valid_input(
        "Enter note: ", lambda x: not is_empty_string(x), "Note can't be empty"
    )
    record.add_note(title, note)
    Printer().print_note_added(record)


@handle_error
def remove_note(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    record.remove_note(title)
    Printer().print_note_removed(title)


@handle_error
def change_note(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    if not record.is_note_exist(title):
        raise KeyError(f"The note with this title '{title}' does not exist.")
    note = get_valid_input(
        "Enter new note: ", lambda x: not is_empty_string(x), "Note can't be empty"
    )
    record.change_note(title, note)
    Printer().print_note_changed(record)


@handle_error
def change_note_title(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    if not record.is_note_exist(title):
        raise KeyError(f"The note with this title '{title}' does not exist.")
    new_title = get_valid_input(
        "Enter new title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    record.change_note_title(title, new_title)
    Printer().print_note_changed(record)


@handle_error
def find_note(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    Printer().print_note_found(record.find_note(title))


@handle_error
def add_tag(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    record = book.find(name)
    title = get_valid_input(
        "Enter note title: ", lambda x: not is_empty_string(x), "Title can't be empty"
    )
    if not record.is_note_exist(title):
        raise KeyError(f"The note with this title '{title}' does not exist.")
    tag = get_valid_input(
        "Enter tag: ", lambda x: not is_empty_string(x), "Tag can't be empty"
    )
    record.add_tag(title, tag)
    Printer().print_tag_added(record, title, tag)


@handle_error
def find_tag(args, book):
    if len(args) == 0:
        raise IndexError("Enter tag")
    tag = " ".join(args)
    notes = book.find_notes_by_tag(tag)
    Printer().print_notes_found(notes)


@handle_error
def add_email(args, book):
    if len(args) == 0:
        raise IndexError("Enter name ")
    name = " ".join(args)
    contact = book.find(name)
    email = get_valid_input(
        "Enter email: ", lambda x: Email.is_valid(x), "Invalid email address"
    )
    contact.set_email(email)
    Printer().print_email_added(contact)


@handle_error
def remove_email(args, book: AddressBook):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    contact.remove_email()
    Printer().print_email_removed(contact)


@handle_error
def change_email(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    email = get_valid_input(
        "Enter email: ", lambda x: Email.is_valid(x), "Invalid email address"
    )
    contact.set_email(email)
    Printer().print_email_changed(contact)


@handle_error
def add_birthday(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    birthday = get_valid_input(
        "Enter birthday: ",
        lambda x: Birthday.is_valid(x),
        "Please enter a valid birthday in the format dd.mm.yyyy",
    )
    contact.set_birthday(birthday)
    Printer().print_birthday_added(contact)


@handle_error
def remove_birthday(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    contact.remove_birthday()
    Printer().print_birthday_removed(contact)


@handle_error
def change_birthday(args, book):
    if len(args) == 0:
        raise IndexError("Please enter a name.")
    name = " ".join(args)
    contact = book.find(name)
    birthday = get_valid_input(
        "Enter birthday: ",
        lambda x: Birthday.is_valid(x),
        "Please enter a valid birthday in the format dd.mm.yyyy",
    )
    contact.set_birthday(birthday)
    Printer().print_birthday_changed(contact)


@handle_error
def get_birthdays_within_future_range(days, book, is_strict_birthday_date=False):
    today = datetime.now()
    birthdays = defaultdict(list)

    for record in book.values():
        if record.birthday:
            birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y")
            if not is_strict_birthday_date:
                user_delta = (birthday_date.replace(year=today.year) - today).days + 1

                if 0 <= user_delta <= days:
                    if get_day_of_week_from_date(birthday_date) == "Saturday":
                        user_delta += 2
                    elif get_day_of_week_from_date(birthday_date) == "Sunday":
                        user_delta += 1

                    next_birthday = get_day_of_week_from_date(
                        today + timedelta(days=user_delta)
                    )
                    birthdays[next_birthday].append(record.name)
            else:
                days_until_birthday = (
                    birthday_date.replace(year=today.year) - today
                ).days + 1
                if days_until_birthday < 0:
                    days_until_birthday = (
                        birthday_date.replace(year=today.year + 1) - today
                    ).days + 1
                if days_until_birthday == int(days):
                    birthdays[f"Birthday in {days}"].append(record.name)

    Printer().print_birthdays_found(birthdays)


@handle_error
def get_birthdays_within_next_week(book):
    days_in_week = 7
    birthdays_within_week = get_birthdays_within_future_range(days_in_week, book, False)
    if birthdays_within_week:
        birthdays_string = ""
        for day, names in birthdays_within_week.items():
            birthdays_string += f"{day}: {', '.join(str(name) for name in names)}\n"
        return birthdays_string
    else:
        return "No upcoming birthdays within next week."


@handle_error
def birthdays(args, book):
    if len(args) < 1:
        return get_birthdays_within_next_week(book)
    elif len(args) == 1:
        birthdays = get_birthdays_within_future_range(args[0], book, True)
        if birthdays:
            birthdays_string = ""
            for day, names in birthdays.items():
                birthdays_string += f"{day}: {', '.join(str(name) for name in names)}\n"
            return birthdays_string
        else:
            return f"No one has a birthday {args[0]} days from today."
    else:
        raise IndexError(
            "Enter no arguments to get birthdays within next week or enter specific number to see who has birthday then"
        )


@handle_error
def show_help():
    Printer().print_help(command_descriptions)


def main():
    book = AddressBook.read_from_file() or AddressBook()
    printer = Printer()
    session = PromptSession(completer=CommandCompleter())

    printer.welcome()
    printer.print_help(command_descriptions)

    while True:
        styled_prompt = printer.get_styled_prompt("Enter a command: ")
        user_input = session.prompt(styled_prompt)
        command, *args = parse_input(user_input, lower=True)

        if command in ["close", "exit"]:
            book.save_to_file()
            Printer().print_exit()
            break
        elif command == "hello":
            Printer().print_hello()
        elif command == "add":
            add_contact(args, book)
        elif command == "find":
            find_contact(args, book)
        elif command == "change":
            change_contact(args, book)
        elif command == "add-phone":
            add_phone(args, book)
        elif command == "change-phone":
            change_phone(args, book)
        elif command == "remove-phone":
            remove_phone(args, book)
        elif command == "remove":
            remove_contact(args, book)
        elif command == "phone":
            get_contact_phones(args, book)
        elif command == "add-address":
            add_address(args, book)
        elif command == "change-address":
            change_address(args, book)
        elif command == "remove-address":
            remove_address(args, book)
        elif command == "all":
            get_all_contacts(book)
        elif command == "add-note":
            add_note(args, book)
        elif command == "remove-note":
            remove_note(args, book)
        elif command == "change-note":
            change_note(args, book)
        elif command == "change-note-title":
            change_note_title(args, book)
        elif command == "find-note":
            find_note(args, book)
        elif command == "add-tag":
            add_tag(args, book)
        elif command == "find-tag":
            find_tag(args, book)
        elif command == "add-email":
            add_email(args, book)
        elif command == "remove-email":
            remove_email(args, book)
        elif command == "change-email":
            change_email(args, book)
        elif command == "add-birthday":
            add_birthday(args, book)
        elif command == "remove-birthday":
            remove_birthday(args, book)
        elif command == "change-birthday":
            change_birthday(args, book)
        elif command == "birthdays":
            birthdays(args, book)
        elif command == "help":
            show_help()
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()

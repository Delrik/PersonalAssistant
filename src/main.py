from collections import defaultdict
from models.address_book import AddressBook
from models.printer import Printer
from models.completer import CommandCompleter
from prompt_toolkit import PromptSession
from datetime import timedelta, datetime


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


def get_day_of_week_from_date(input_date):
    return input_date.strftime("%A")


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
    contact.set_birthday(new_birthday)

    # TODO: Print
    return f"Birthday changed for {name}."


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

    return birthdays


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
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "remove-birthday":
            print(remove_birthday(args, book))
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            Printer().print_invalid_command()


if __name__ == "__main__":
    main()

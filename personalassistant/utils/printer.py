from rich.console import Console
from rich.table import Table
from rich.text import Text
from prompt_toolkit import HTML


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Printer(metaclass=SingletonMeta):
    def __init__(self):
        self.console = Console()

    def get_styled_input(self, prompt_text):
        return self.console.input(f"[blue]➤ {prompt_text}")

    def get_styled_prompt(self, prompt_text):
        return HTML(f"<ansiblue>➤ {prompt_text}</ansiblue>")

    def welcome(self):
        self.console.print(
            "\n[bold yellow]🌟✨ Welcome! ✨🌟[/bold yellow]\n"
            "[bold green]👋 You've just entered your Personal Assistant! 👋[/bold green]\n"
            "[bold cyan]🚀 Ready to assist you with your tasks! 🚀[/bold cyan]\n",
            style="bold",
        )

    def print_hello(self):
        self.console.print(
            "\n[bold blue]💡 Hello! How may I assist you today? 💡[/bold blue]\n"
            "[bold aqua]🌐 Feel free to ask me anything or run '[bold]help[/bold]' to see all commands! 🌐[/bold aqua]\n"
            "[bold sky_blue]🤖 Your Personal Assistant is at your service! 🤖[/bold sky_blue]\n",
            style="bold",
        )

    def print_exit(self):
        self.console.print(
            "\n[bold red]🌹 Farewell and take care! 🌹[/bold red]\n"
            "[bold magenta]👋 Good bye! See you soon! 👋[/bold magenta]\n",
            style="bold",
        )

    def print_invalid_command(self):
        self.console.print(
            "Invalid command. Please enter a valid command.", style="yellow"
        )

    def print_is_already_exist(self, value):
        self.console.print(f"The '{value}' is already exists.", style="yellow")

    def print_is_not_exist(self, value):
        self.console.print(f"The '{value}' is not exists.", style="yellow")

    def print_contact(self, contact):
        self.console.print(contact)

    def print_all_contacts(self, book):
        table = Table(show_header=True, header_style="yellow", expand=True)
        table.add_column("Name", style="blue")
        table.add_column("Phones", style="blue")
        table.add_column("Address", style="blue")
        table.add_column("Email", style="blue")
        table.add_column("Birthday", style="blue")
        table.add_column("Notes", style="blue")

        for record in book.data.values():
            phone_numbers = ", ".join(str(phone) for phone in record.phones)
            address = str(record.address) if record.address else ""
            email = str(record.email) if record.email else ""
            birthday = str(record.birthday) if record.birthday else ""

            notes_text = Text()
            for note in record.notes:
                notes_text.append(f"{note.title}: ", style="bold blue")
                notes_text.append(f"{note.text} ", style="blue")
                if note.tags:
                    formatted_tags = ", ".join(note.tags)
                    notes_text.append(formatted_tags, style="green")
                notes_text.append("\n")

            table.add_row(
                record.name.value, phone_numbers, address, email, birthday, notes_text
            )

        self.console.print(table)

    def print_error(self, error):
        error_message = f"[red]{error}[/red]"
        self.console.print(error_message)

    def print_contact_added(self, record):
        self.console.print(f"Contact added successfully:\n", style="green")
        self.console.print(record)

    def print_contact_deleted(self, name):
        self.console.print(
            f"Contact '{name}' deleted successfully.", style="red")

    def print_contact_changed(self, record):
        self.console.print(f"Contact updated successfully:\n", style="blue")
        self.console.print(record)

    def print_email_changed(self, record):
        self.console.print(f"Email updated successfully:\n", style="cyan")
        self.console.print(record)

    def print_note_added(self, record):
        self.console.print(f"Note added successfully:\n", style="green")
        self.console.print(record)

    def print_note_removed(self, title):
        self.console.print(f"Note '{title}' removed successfully", style="red")

    def print_note_changed(self, record):
        self.console.print(f"Note updated successfully:\n", style="blue")
        self.console.print(record)

    def print_note_found(self, note):
        self.console.print(f"Note found:\n", style="magenta")
        self.console.print(note)

    def print_notes_found(self, notes):
        for note in notes:
            self.console.print(f"Note found:\n", style="magenta")
            self.console.print(note[0], style="bold blue")
            self.console.print(note[1])

    def print_tag_added(self, record, title, tag):
        self.console.print(f"Tag added successfully:\n", style="green")
        self.console.print(record)

    def print_email_added(self, record):
        self.console.print(f"Email added successfully:\n", style="green")
        self.console.print(record)

    def print_email_removed(self, record):
        self.console.print(f"Email removed successfully:\n", style="red")
        self.console.print(record)

    def print_email_changed(self, record):
        self.console.print(f"Email updated successfully:\n", style="cyan")
        self.console.print(record)

    def print_birthday_added(self, record):
        self.console.print(f"Birthday added successfully:\n", style="green")
        self.console.print(record)

    def print_birthday_removed(self, record):
        self.console.print(f"Birthday removed successfully:\n", style="red")
        self.console.print(record)

    def print_birthday_changed(self, record):
        self.console.print(f"Birthday updated successfully:\n", style="cyan")
        self.console.print(record)

    def print_birthdays_found(self, birthdays):
        table = Table(show_header=True, header_style="yellow", expand=True)
        table.add_column("Day", style="blue")
        table.add_column("Names", justify="left", style="cyan")

        for day, names in birthdays.items():
            names_str = ", ".join([str(name) for name in names])
            table.add_row(day, names_str)

        self.console.print(table)

    def print_phone_added(self, record):
        self.console.print(
            f"Phone number added successfully:.\n", style="green")
        self.console.print(record)

    def print_contact_phones(self, phone_numbers):
        self.console.print("Phone numbers for the contact:", style="blue")
        for phone in phone_numbers:
            self.console.print(phone, style="cyan")

    def print_phone_changed(self, record):
        self.console.print(
            f"Phone number updated successfully:\n", style="blue")
        self.console.print(record)

    def print_phone_removed(self, record):
        self.console.print(
            f"Phone number removed successfully:\n", style="red")
        self.console.print(record)

    def print_address_added(self, record):
        self.console.print(f"Address added successfully:\n", style="green")
        self.console.print(record)

    def print_address_changed(self, record):
        self.console.print(f"Address updated successfully:\n", style="green")
        self.console.print(record)

    def print_address_removed(self, record):
        self.console.print(f"Address removed successfully:\n", style="red")
        self.console.print(record)

    def print_help(self, command_descriptions):
        table = Table(show_header=True, header_style="blue")
        table.add_column("Command", style="yellow", width=30)
        table.add_column("Description", justify="left")

        for command, (description, args) in command_descriptions.items():
            command_with_args = f"{command} {args}" if args else command
            table.add_row(command_with_args, description)
            table.add_row("", "")

        self.console.print(table)

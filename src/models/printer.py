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

    def print_phone_added(self):
        print("Phone added.")

    def print_phone_changed(self):
        print("Phone changed.")

    def print_phone_removed(self):
        print("Phone removed.")

    def print_address_added(self):
        print("Address added.")

    def print_address_changed(self):
        print("Address changed.")

    def print_address_removed(self):
        print("Address removed.")

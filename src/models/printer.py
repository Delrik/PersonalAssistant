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

    def print_all_contacts(self, book):
        for record in book.data.values():
            print(record)

    def print_error(self, error):
        print(error)

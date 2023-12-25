from .field import Field
import re


class Email(Field):
    def __init__(self, email):
        self.validate_email(email)
        super().__init__(email)

    @staticmethod
    def validate_email(email):
        if not Email.is_valid(email):
            raise ValueError(f"{email} is not a valid email address.")

    @staticmethod
    def is_valid(email):
        pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not re.match(pattern, email):
            return False
        return True

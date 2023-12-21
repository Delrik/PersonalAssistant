from collections import UserDict, defaultdict
import pickle
from datetime import timedelta, datetime

from .record import Record


class AddressBook(UserDict):
    def get_day_of_week_from_date(self, input_date):
        return input_date.strftime("%A")

    def add_record(self, name, phone):
        if name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' already exists.")
        record = Record(name)
        record.add_phone(phone)
        self.data[name] = record

    def set_address(self, name, address):
        record = self.find(name)
        record.set_address(address)

    def get_birthdays_per_week(self):
        today = datetime.now()
        this_week_birthdays = defaultdict(list)

        for record in self.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y')
                user_delta = (birthday_date.replace(year=today.year) - today).days
                if 7 > user_delta >= 0:
                    if self.get_day_of_week_from_date(birthday_date) == 'Saturday':
                        user_delta += 2
                    elif self.get_day_of_week_from_date(birthday_date) == 'Sunday':
                        user_delta += 1
                    next_birthday = self.get_day_of_week_from_date(today + timedelta(days=user_delta))
                    this_week_birthdays[next_birthday].append(record.name.value)

        return this_week_birthdays

    def find(self, name) -> Record:
        if not name in self.data:
            raise KeyError(
                f"The contact with this name '{name}' does not exist.")
        return self.data[name]

    def findAll(self):
        if len(self.data) == 0:
            raise KeyError(f"The contact list is empty.")
        return [f"{name}: {self.data[name].phone}" for name in self.data.keys()]

    def save_to_file(self):
        with open("db.bin", "wb") as file:
            pickle.dump(self, file)

    def read_from_file():
        try:
            with open("db.bin", "rb") as file:
                return pickle.load(file)
        except:
            return None

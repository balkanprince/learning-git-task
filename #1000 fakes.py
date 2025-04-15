#1000 fakes

from faker import Faker
from datetime import datetime

fake = Faker("pl_PL")


# Dekorator do mierzenia czasu wykonania
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        print(f"Czas wykonania: {elapsed_time:.3f} sekund")
        return result
    return wrapper


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


@measure_time
def generate_1000_contacts():
    contacts = []
    for _ in range(1000):
        contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            email=fake.email()
        )
        contacts.append(contact)
    return contacts


my_1000_contacts = generate_1000_contacts()

from faker import Faker
import random

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


def create_contacts(contact_type, number):
    contacts = []
    for _ in range(number):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()

        if contact_type == "base":
            contact = BaseContact(first_name, last_name, phone, email)
        elif contact_type == "business":
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone, email, position, company, business_phone)
        else:
            raise ValueError("Unknown contact type")

        contacts.append(contact)

    return contacts



my_contacts = create_contacts("business", 5)

print("\nWizytówki:")
for contact in my_contacts:
    print(str(contact))

print("\nSortowanie według imienia:")
for contact in sorted(my_contacts, key=lambda c: c.first_name):
    print(contact)

print("\nSortowanie według nazwiska:")
for contact in sorted(my_contacts, key=lambda c: c.last_name):
    print(contact)

print("\nSortowanie według e-maila:")
for contact in sorted(my_contacts, key=lambda c: c.email):
    print(contact)

print("\nPrzykładowy kontakt:")
my_contacts[0].contact()
print("Długość etykiety:", my_contacts[0].label_length)

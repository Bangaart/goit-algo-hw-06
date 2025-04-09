from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __repr__(self):
        return str(self.value)


class Phone(Field):

    def phone_validation(self):
        if len(self.value) == 10 and self.value.isdigit():
            return self.value
        else:
            raise ValueError ("Phone number should be 10 digits and don't contain alphabet symbols")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone).phone_validation())

    def edit_phone(self, old_number, new_number):
        if old_number in self.phones:
            self.phones[self.phones.index(old_number)] = new_number
        else:
            raise ValueError ("Check correctness of the number ")

    def find_phone(self, phone):
        if phone in self.phones:
            return phone

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record_object):
        self.data[str(record_object.name)] = record_object.phones

    def find(self, name):
        if name in self.data.keys():
            a = Record(name)
            a.phones = self.data[name]
            return a


    def delete(self, name):
        del self.data[name]

    def __str__(self):
        full_string = ''
        for i in self.data:
            full_string += f"Contact name : {i}, phones: {'; '.join(p for p in self.data[i])}\n"
        return full_string

    # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

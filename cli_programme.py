from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_number, new_number):
        phone_obj = self.find_phone(old_number)
        if  phone_obj:
            self.add_phone(new_number)
            self.remove_phone(old_number)
        else:
            raise ValueError ("Check correctness of the number ")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record_object):
        self.data[record_object.name.value] = record_object

    def find(self, name):
        if name in self.data.keys():
            return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def __str__(self):
        result = ""
        for name, value in self.data.items():
            phones = ";".join(p.value for p in value.phones)
            result += f"Contact name : {name}, phones: {phones}\n"
        return result.strip()


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
john.remove_phone("1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")



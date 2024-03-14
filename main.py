# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Human:
    def __init__(self, full_name, date_of_birth, phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def input_data(self):
        self.full_name = input("Введіть піб: ")
        self.date_of_birth = input("Введіть дату народження: ")
        self.phone_number = input("Введіть контактний телефон: ")
        self.city = input("Введіть місто: ")
        self.country = input("Введіть країну: ")
        self.home_address = input("Введіть домашню адресу: ")

    def display(self):
        print("піб:", self.full_name)
        print("дата народження:", self.date_of_birth)
        print("контактний телефон:", self.phone_number)
        print("місто:", self.city)
        print("країна:", self.country)
        print("домашня адреса:", self.home_address)

    def update_data(self, attribute):
        if attribute == "піб":
            self.full_name = input("Введіть новий піб: ")
            print("Інформація оновлена.")
        elif attribute == "дата народження":
            self.date_of_birth = input("Введіть нову дату народження: ")
            print("Інформація оновлена.")
        elif attribute == "контактний телефон":
            self.phone_number = input("Введіть новий контактний телефон: ")
            print("Інформація оновлена.")
        elif attribute == "місто":
            self.city = input("Введіть нове місто: ")
            print("Інформація оновлена.")
        elif attribute == "країна":
            self.country = input("Введіть нову країну: ")
            print("Інформація оновлена.")
        elif attribute == "домащня адреса":
            self.home_address = input("Введіть нову домашню адресу: ")
            print("Інформація оновлена.")
        else:
            print("Невірний ввід.")

person = Human("", "", "", "", "", "")
person.input_data()
print("\nІнформація про людину:")
person.display()

while True:
    information_to_change = input("\nВведіть яку інформацію ви хочете змінити (або 0, якщо нічого): ").lower()
    if information_to_change == "0":
        print("Програма завершена :(")
        break

    person.update_data(information_to_change)

print("\nОновлена інформація: ")
person.display()

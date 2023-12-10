from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    first_name = "Joe"
    last_name = "White"
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера.")
        except ValueError:
            print("Номер должен состоять только из цифр.")
        except LenNumberError as error:
            print(error)
            continue
        is_valid_phone = True
    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - менеджер контекста
    with open(file_name, 'w', encoding="UTF-8") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding="UTF-8") as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, contacts_list):
    result = read_file(file_name)
    new_dictionary = {"Имя": contacts_list[0], "Фамилия": contacts_list[1], "Телефон": contacts_list[2]}
    result.append(new_dictionary)
    with open(file_name, 'w', encoding="UTF-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(result)


def main():
    while True:
        file_name = "White pages.csv"
        command = input("Введите команду:")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его.")
                continue
            print(*read_file(file_name))


main()

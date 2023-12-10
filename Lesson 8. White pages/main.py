from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    first_name = "Joe"
    second_name = "Antony"
    last_name = "White"
    phone_number = 0
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
    return [first_name, second_name, last_name, phone_number]


def create_file(file_name):
    # with - менеджер контекста
    with open(file_name, 'w', encoding="UTF-8") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Отчество", "Фамилия", "Телефон"])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding="UTF-8") as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, contacts_list):
    result = read_file(file_name)
    new_dictionary = {"Имя": contacts_list[0], "Отчество": contacts_list[1],
                      "Фамилия": contacts_list[2], "Телефон": contacts_list[3]}
    result.append(new_dictionary)
    with open(file_name, 'w', encoding="UTF-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Отчество", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(result)


def required_length_string(text, required_length):
    text = str(text)
    current_length = len(text)
    if current_length >= required_length:
        return text[0:required_length]
    else:
        return text+" "*(required_length-current_length)


def dictionaries_chars_count(dictionaries_list):
    result = {"Имя": 3, "Фамилия": 7, "Отчество": 8, "Телефон": 11, "№": len(str(len(dictionaries_list)))}
    for current_dictionary in dictionaries_list:
        for current_key in current_dictionary.keys():
            current_value = len(current_dictionary.get(current_key))
            saved_value = result.get(current_key)
            if saved_value is None:
                result[current_key] = current_value
            elif current_value > saved_value:
                result[current_key] = current_value
    return result


def print_dictionaries_list(dictionaries_list):
    chars_count = dictionaries_chars_count(dictionaries_list)
    slim_end = '|'
    wide_end = " | "
    result = f"| {required_length_string('№', chars_count['№'])}" + wide_end
    for key in dictionaries_list[0].keys():
        result += (required_length_string(key, chars_count[key]) + wide_end
        print()
    print(f"|-{'-' * (chars_count['№'] + 1)}", end='|')
    for key in dictionaries_list[0].keys():
        print("-" * (chars_count[key] + 2), end='|')
    print()
    i = 1
    for contact in dictionaries_list:
        print(f"| {required_length_string(i, chars_count['№'])}", end=" | ")
        for key in contact.keys():
            print(required_length_string(contact[key], chars_count[key]), end=' | ')
        i += 1
        print()


def main():
    while True:
        file_name = "White pages.csv"
        command = input("Enter \"r\" to read white pages, \"w\" to write, \"q\" to exit program: ")
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
            print(f"Список контактов из файла {file_name}:")
            contacts_list = read_file(file_name)
            print_dictionaries_list(contacts_list)


main()

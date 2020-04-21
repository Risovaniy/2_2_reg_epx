from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def phone(line):
    phone_pattern = "(\+7|8|7*)+(\s*)(\(\d{3}\))(\s*)(\d{3})(-+|\s*)(\d{2})(-+|\s*)(\d{2})"
    result = re.sub(phone_pattern, r"+7\3\5-\7-\9", line[5])
    line[5] = result
    if len(line[5]) > 16:
        phone_pattern = "(\+7\(\d{3}\)\d{3}-\d{2}-\d{2})(-+|\s*|\s*доб\.|доб)(\d+)"
        result = re.sub(phone_pattern, r"\1 доб.\3", line[5])
        line[5] = result


def names(line):
    if len(line[0]) != 0 and len(line[1]) != 0 and len(line[2]) != 0:
        print(f'Contact {line[0]} {line[1]} {line[2]} is ok')
    elif len(line[1]) == 0 and len(line[2]) == 0:
        result = re.split(r'[;,\s]+', line[0])
        line[0] = result[0]
        line[1] = result[1]
        line[2] = result[2]
        print(f'Contact {line[0]} {line[1]} {line[2]} fixed(from lastname)')
    elif len(line[2]) == 0:
        result_0 = re.split(r'[;,\s]+', line[0])
        result_1 = re.split(r'[;,\s]+', line[1])
        if len(result_0) == 2:
            line[0] = result_0[0]
            line[1] = result_0[1]
            line[2] = result_1[0]
            print(f'Contact {line[0]} {line[1]} {line[2]} fixed(2 from lastname)')
        else:
            line[0] = result_0[0]
            line[1] = result_1[0]
            line[2] = result_1[1]
            print(f'Contact {line[0]} {line[1]} {line[2]} fixed(2 from firstname)')


def check_information(line):
    cell_without_info = list()
    if len(line[3]) == 0:
        cell_without_info.append(3)
    if len(line[4]) == 0:
        cell_without_info.append(4)
    if len(line[6]) == 0:
        cell_without_info.append(6)
    return cell_without_info


def checking_of_douples(line_1, line_2):
    if line_1 != line_2:
        if line_1[5] == line_2[5]:
            return True


def fix_doubles(line):
    for check_line in contacts_list:
        if checking_of_douples(line, check_line):
            for cell in check_information(line):
                line[cell] = check_line[cell]
            contacts_list.remove(check_line)


# name_pattern = "([А-Я]{1}[а-яё]+)\s+([А-Я]{1}[а-яё]+)\s+([А-Я]{1}[а-яё]+)"
# phone_pattern = "(\+7|8)*(\s*)(\(\d+\))(\s*)(\d+)(-+|\s)(\d+)(-+|\s)(\d+)(-+|\s*)(\d*)"


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

for line in contacts_list:
    phone(line)
    names(line)
    fix_doubles(line)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)

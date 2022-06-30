"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.
Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import json
from hashlib import sha256
from os.path import join, dirname


def read_data():
    with open(join(dirname(__file__), "db.json"), 'r') as j_file:
        data = json.load(j_file)

    return data


def write_data(data):
    with open(join(dirname(__file__), "db.json"), 'w', encoding='utf-8') as j_file:
        json.dump(data, j_file, indent=4, ensure_ascii=False)
    return


def get_hash():
    login = input('Введи логин: ')
    pswd = input('Введи пароль: ')
    hash_obj = sha256(login.encode() + pswd.encode()).hexdigest()

    return login, hash_obj


def log_in():
    login, password = get_hash()
    data = read_data()
    if login in data:
        if data[login] == password:
            print(f'Привет, {login}')
        else:
            print('Неправильный пароль. ПОпробуйте позже')
    else:
        print('Вы не зарегистрированы')
        return


def register():
    login, password = get_hash()
    data_dict = read_data()
    if login in data_dict:
        print('Вы уже зарегистрированы. Пожалуйста, войдите')
    else:
        data_dict[login] = password
        write_data(data_dict)
        print('Спасибо за регистрацию!')


def main():
    answer = input('вход / регистрация ? : ')
    if answer == 'вход':
        log_in()
    elif answer == 'регистрация':
        register()


if __name__ == '__main__':
    main()

def last_name():
    return input('Введите фамилию ')


def first_name():
    return input('Введите имя ')


def group():
    return input('Введите класс ')


def read(line_group: str, id: str):
    print(f'Запись с ID {id}: {line_group}')


def id():
    return input('Введите ID ')


def invalid_id():
    print('Вы ввели не верный ID ')


def print_with_id(with_id: str):
    print(with_id)


def print_without_id(without_id: str):
    print(without_id)


def menu_print():
    print('''
1 Создать запись 
2 Извлечь запись по ID 
3 Обновить запись по ID 
4 Удалить запись по ID 
5 Экспорт в CSV файл 
6 Импорт из CSV файла с ID 
7 Импорт из CSV файла без ID 
8 Выход 
''')


def menu():
    return input('Выберете пункт меню ')


def not_menu():
    print('Вы ввели не верный пункт меню')


def exit():
    print()
    print('Программа завершена')

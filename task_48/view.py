def action():
    return input('Введите действие (ввод данных - wr, считать данныу - rd, экспорт из файла - ex) ')

def name_phonebook():
    return input('Введите имя файла телефонной кинги ')

def file_name():
    return input('Введите имя файла для экспорта ')

def data_in_file(record):
    print('Телефонная книга ')
    print(record)

def data()->list:
    return [input('Введите Фамилию '), input('Введите Имя '), input('Введите телефон '), input('Введите описание ')]
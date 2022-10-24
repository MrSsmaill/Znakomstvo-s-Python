# Задача 39. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста


import moduls


def list_del_elements(string_list):
    index = set()
    for i in range(len(string_list)):
        for value in item:
            if string_list[i].find(value) != -1:
                index.add(i)
    return index


def del_elements(index):
    index = list(index)
    for i in range(len(index)):
        string_list.pop(index[i] - i)
    return string_list


item = "ase"
string_list = moduls.read_data("task_39.1.txt")
moduls.write_data("task_39.2.txt", string_list)

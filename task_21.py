# Задача 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

string_list = ["qwe", "asd", "qwe", "qwe", "qwe", "zxc", "ertqwe", ]
item = "qwe"


def string_search(str_list, elem):
    count = 0
    for i in range(len(str_list)):
        if elem == string_list[i]:
            count += 1
            if count == 2:
                print(i)
            elif count <= 1:
                print(-1)


string_search(string_list, item)

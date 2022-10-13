# Задача 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

str_list = ["qwe", "asd", "zxc", "12", "qwe", "ertqwe", ]

for i in str_list:
    if i.isdigit():
        flag = True
        break
    else:
        flag = False
print(flag)

# Задача 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число '))
bin_num = ''
while num != 0:
    bin_num = str(num % 2) + bin_num
    num = int(num / 2)
print(bin_num)

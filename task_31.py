# Задача 31 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.

flag = 1  # Выбор числа

num_1 = 147420
num_2 = 374220

if flag == 1:
    num = num_1
elif flag == 2:
    num = num_2
number = num
num_list = set()
i = 2
while i * i <= num:
    if num % i == 0:
        num_list.add(i)
        num //= i
    else:
        i += 1
if num > 1:
    num_list.add(num)
print('simple_number({}) => {};'.format(number, list(num_list)))

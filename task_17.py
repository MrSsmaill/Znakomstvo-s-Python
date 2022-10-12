"""Задача 17 Задайте список из элементов, заполненных числами из промежутка [-N, N].
Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
Найдите произведение элементов списка в указанном диапазоне индексов"""

import random
import re


def interval_input():
    interval = input('Введите интервал ')
    interval = re.split(";| |,|\n ", interval)
    interval.append(int(interval.pop(0)))
    interval.append(int(interval.pop(0)))
    interval = interval[0:2]
    print(interval)
    return interval


num = int(input('Введите N '))
num_list = []
for i in range(num * 2 + 1):
    num_list.append(random.randint(-num, num))
print(num_list)
num_interval = []
num_interval = interval_input()

while True:
    if num_interval[1] < len(num_list) and num_interval[0] < num_interval[1] and num_interval[0] > 0:
        break
    else:
        print('Ввели не верный интервал ')
        num_interval.clear()
        num_interval = interval_input()

num_sum = 0
for i in range(num_interval[0] - 1, num_interval[1]):
    num_sum += num_list[i]

print('Суммы элементов в интервале ({};{}) равна {}'.format(num_interval[0], num_interval[1], num_sum))

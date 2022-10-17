# Задача 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

num_list = []
for value in range(5):
    num_list.append(int(random.randint(-9, 9)))
print(num_list)
sum_elem = 0
print('на нечетных позициях элементы ', end='')
for i in range(len(num_list)):
    if i % 2 == 1:
        sum_elem += num_list[i]
        print(num_list[i], ', ', end='')
print(' ответ: {}'.format(sum_elem))

# Задача 32  Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import moduls

num_list = moduls.random_num_list(10, 0, 10)
print(num_list)
result = set(num_list)
print(result)

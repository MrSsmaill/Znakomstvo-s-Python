# Задача 23.  Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

num_list = []
for value in range(int(random.randint(3, 7))):
    num_list.append(int(random.randint(-9, 9)))
print(num_list)
product_elem = []
for i in range(len(num_list) - int(len(num_list) / 2)):
    product_elem.append(int(num_list[i])*num_list[len(num_list)-1-i])
print(product_elem)

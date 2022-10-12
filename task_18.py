# Задача 18 Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.

import random

num = 5
num_list = []
for i in range(num * 2):
    num_list.append(random.randint(-num, num))
print(num_list)
num_list_result = []

for i in range(len(num_list)):
    value = []
    value.extend(random.choices(num_list))
    num_list_result.insert(i, value[0])
    num_list.pop(num_list.index(value[0]))
    value.clear()

print(num_list_result)

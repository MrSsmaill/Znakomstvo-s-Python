#Задача 27. Задайте строку из набора чисел.Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

import random

num_random = []
for value in range(int(random.randint(3, 9))):
    num_random.append(str(random.randint(-10, 9)))
num_str=' '.join(num_random)
num_list=num_str.split()
print(num_list)

print('Болшее {}, меньшее {}'.format(max(num_list),min(num_list)))
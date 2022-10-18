# Задача 33  Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100

import random
import moduls


def polynomial(k):
    odds = moduls.random_num_list(k + 1, 0, 100)
    list_polyn = []
    while odds[k] == 0:
        odds.insert(k, int(random.randint(0, 100)))
    for i in range(k + 1):
        if i >= 2 and odds[i] != 0:
            list_polyn.append(str(odds[i]) + 'x^' + str(i))
        elif i == 1 and odds[i] != 0:
            list_polyn.append(str(odds[i]) + 'x')
        elif i == 0 and odds[i] != 0:
            list_polyn.append(str(odds[i]))
    list_polyn.reverse()
    str_polyn = '+'.join(list_polyn)
    str_polyn += '=0'
    return str_polyn


my_file = open("polynomial_1.txt", "w")
my_file.write(polynomial(3))
my_file.close()

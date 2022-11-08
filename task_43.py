'''Задача 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] -> [2, 10]
[1, 2, 3, 5, 1, 5, 3, 10, 1] -> [2, 10]
[1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9] -> [4,5,7,9]
Примечание:
В этой задаче есть вариант решения "в лоб"(используя списки) или решения ээфективного(используя множества)'''

from time import perf_counter
from random import randint

def unique_lst(lst):
    return [el for el in lst if lst.count(el) == 1]


def unique_set(lst):
    unique = set()
    not_unique = set()
    for el in lst:
        if el in unique:
            unique.remove(el)
            not_unique.add(el)
        elif el not in not_unique:
            unique.add(el)
    return list(unique)

if __name__ == "__main__":
    n = 10
    lst = [randint(-100,100) for _ in range(n)]

    t1 = perf_counter()
    print(unique_lst(lst))
    t2 = perf_counter()
    print(unique_set(lst))
    t3 = perf_counter()
    print(lst)
    print(f'list: {t2-t1:.2e} set: {t3-t2:.2e} rel = {(t3-t2)/(t2-t1):.9f}')
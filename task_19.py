# Задача 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from time import time, perf_counter

num_list=[]
for i in range(10):
    for j in range(10):
        value = perf_counter()*100000
        value -= int(value)
        value = perf_counter()*100000
        value -= int(value)
        value *= 10
        num_list.append(int(value))
    print(num_list)
    num_list.clear()



# def rnd(prev=None):
#     if prev is None: prev = int(time())
#     rez = (prev * 1103515245 + 12345) % 32767
#     return rez
#
# # a0 = int(time())
# a1 = rnd()
# a2 = rnd(a1)
# a3 = rnd(a2)

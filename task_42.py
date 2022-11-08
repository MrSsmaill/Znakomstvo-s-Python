'''Задача 41. Напишите программу вычисления арифметического выражения заданного строкой.
Возможные операции в выражении только: +,-,/,*. приоритет операций стандартный.
Техническое задание:
1) Числа могут быть только целые, любой размерности
2) Унарный оператор минус не рассматриваем, т.е. '-2*3' недопустимо
3) Не используйте функцию eval.
4) Программа возвращает результат вычисления в виде числа.
Общая схема решения:
1) Выделить части алгоритма, использовать для них функции.
2) Протестировать функции на множестве примеров, убедиться в правильности работы. Создать "модуль тестирования".
Пример:
2+2 -> 4
1+2*3 -> 7
1-2*3 -> -5
1-2*33 -> -65
2-1+3*7 -> 10
1-2*3/5 -> -0.2
1+2*3-6*5+78 -> 55 '''

my_str = '1-2*33'


def pars_str(my_str: str) -> list:
    print(my_str)
    my_list = []
    temp = 0
    for idx, elem in enumerate(my_str):
        if elem in '+-/*':
            my_list.append(int(my_str[temp:idx]))
            my_list.append(elem)
            temp = idx + 1
    my_list.append(int(my_str[temp:]))
    return my_list

def zn(value:str):



def run(my_list:list):
    tmp_list=my_list.copy()
    idx=0
    while idx < len(tmp_list):
        elem = tmp_list[idx]
        if elem == '*':
            tmp_list[idx - 1] *= tmp_list[idx + 1]
            tmp_list.pop(idx)
            tmp_list.pop(idx)
            idx-=1
        elif elem == '/':
            tmp_list[idx - 1] /= tmp_list[idx + 1]
            tmp_list.pop(idx)
            tmp_list.pop(idx)
            idx-=1
        idx+=1
    idx = 0
    while idx < len(tmp_list):
        elem = elem = tmp_list[idx]
        if elem == '+':
            tmp_list[idx - 1] += tmp_list[idx + 1]
            tmp_list.pop(idx)
            tmp_list.pop(idx)
            idx -= 1
        elif elem == '-':
            tmp_list[idx - 1] -= tmp_list[idx + 1]
            tmp_list.pop(idx)
            tmp_list.pop(idx)
            idx -= 1
        idx+=1
    return tmp_list[0]


print(run(pars_str(my_str)))



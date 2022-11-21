def lsm(num_1: int, num_2: int) -> int:
    i = max(num_1, num_2)
    while ((i % num_1 != 0) or (i % num_2 != 0)):
        i += 1
    return i


def parsing(my_str: str) -> list:
    if '/' in my_str:
        new_list = my_str.split('/')
        new_list = [int(el) for el in new_list]
    else:
        new_list = [int(my_str), 1]
    return new_list


def calculate(num_1: list, num_2: list, operat: str) -> list:
    nok = lsm(num_1[1], num_2[1])
    cf_1 = nok // num_1[1]
    cf_2 = nok // num_2[1]
    if operat == '+':
        return [num_1[0] * cf_1 + num_2[0] * cf_2, nok]
    elif operat == '-':
        return [num_1[0] * cf_1 - num_2[0] * cf_2, nok]
    elif operat == '*':
        return [num_1[0] * num_2[0], num_1[1] * num_2[1]]
    elif operat == '/':
        return [num_1[0] * num_2[1], num_1[1] * num_2[0]]

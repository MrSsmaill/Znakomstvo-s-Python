"""# Задача 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
 https://ru.wikipedia.org/wiki/Кодированиедлинсерий
 Создать функцию сжатия строки и функцию восстановления строки."""

sim_str = 'WWJJJHDDDDDPPGRRR'


def rle_algorithm(sim_str: str) -> str:
    sim_list = list(sim_str)
    sim_list.append(' ')
    value = sim_list.pop(0)
    result_list = []
    while len(sim_list) != 0:
        count = 1
        result_list.append(value)
        while value == sim_list[0]:
            value = sim_list.pop(0)
            count += 1
        value = sim_list.pop(0)
        result_list.append(str(count))
    rle_list = []
    i = 0
    while i < len(result_list):
        rle_list.append(result_list[i + 1])
        rle_list.append(result_list[i])
        i += 2
    rle_str = ''.join(rle_list)
    return rle_str


def rle_recovery(rle_str: str) -> str:
    i = 0
    rle_recovery = str()
    while i < len(rle_str):
        rle_recovery += rle_str[i + 1] * int(rle_str[i])
        i += 2
    return rle_recovery


rle = rle_algorithm(sim_str)
recovery = rle_recovery(rle)

print('{} -> {} -> {}'.format(sim_str, rle, recovery))

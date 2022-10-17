# Задача 24. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

num_list = [1.1, 1.2, 3.1, 5, 10.01, 12.00]
print(num_list)
fractional_list = []
for i in range(len(num_list)):
    ost = str(num_list[i])[str(num_list[i]).find('.'):]
    ost = float(ost)
    if str(num_list[i]).find('.') != -1 and ost != 0:
        fractional_list.append(ost)
        max_item = fractional_list[0]
        min_item = fractional_list[0]
for item in fractional_list:
    if item > max_item:
        max_item = item
    elif item < min_item:
        min_item = item
print('Разница между максимальными и минимальными значениями дробной части ', max_item - min_item)

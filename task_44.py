# Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200.
# Использовать comprehensions

def odd_numbers(num) -> list:
    return [item for item in range(num) if item % 2 == 1 and item * item < 200]


print(odd_numbers(20))

"""Режимы игры:

1. игрок & игрок
2. игрок & простой бот
3. игрок & сложный бот
4. простой бот & простой бот
5. простой бот & сложный бот

Очередь будет выбрана случайно"""

mode = 6

import random
import time
import colorama
from termcolor import colored, cprint


def player(sweets, count):
    print(colorama.Fore.GREEN + 'Oсталось {} конфет'.format(sweets))
    num = input(colorama.Fore.GREEN + '{} игрок '.format(count % 2 + 1))
    print()
    while num == '' or int(num) > 28 or int(num) > sweets or int(num) < 1:
        print('ввели не верное колличество')
        num = input('{} игрок '.format(count % 2 + 1))
    sweets -= int(num)
    return sweets


def game(sweets, count, player1, player2):
    while sweets != 0:
        count += 1
        if count % 2 == 0:
            sweets = player1(sweets, count)
        else:
            sweets = player2(sweets, count)
    print(colorama.Style.BRIGHT + colorama.Fore.CYAN +
          '\nВыйграл {} игрок'.format(count % 2 + 1))


def monetka():
    return random.randint(0, 1)


def bot_easy(sweets, count):
    print(colorama.Fore.GREEN + 'Oсталось {} конфет'.format(sweets))
    time.sleep(1)
    a = 28
    if a > sweets:
        a = sweets
    b = random.randint(1, a)
    print(colorama.Fore.YELLOW + 'Бот {} взял {} конфет\n'.format(count % 2 + 1, b))
    sweets -= b
    return sweets


def bot_expert(sweets, count):
    print(colorama.Fore.GREEN + 'Oсталось {} конфет'.format(sweets))
    time.sleep(1)
    a = sweets % 28 - 1
    if a <= 0:
        a = 1
    if 28 >= sweets:
        a = sweets
    print(colorama.Fore.BLUE + 'Бот {} взял {} конфет\n'.format(count % 2 + 1, a))
    sweets -= a
    return sweets


if mode == 1:
    game(220, monetka(), player, player)
elif mode == 2:
    game(220, monetka(), player, bot_easy)
elif mode == 3:
    game(220, monetka(), player, bot_expert)
elif mode == 4:
    game(220, monetka(), bot_easy, bot_easy)
elif mode == 5:
    game(220, monetka(), bot_easy, bot_expert)
else:
    text = colored('Вы указали не правильный режим игры, можно изменить в начале программы', 'red', attrs=['blink'])
    print(text)
    cprint('Hello, Habr!', 'green', 'on_red')

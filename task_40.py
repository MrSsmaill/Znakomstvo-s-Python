'''
Задача 40. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.'''

"""Режимы игры:

1. игрок & игрок
2. игрок & простой бот 
3. игрок & сложный бот 
4. простой бот & простой бот
5. простой бот & сложный бот

Очередь будет выбрана случайно"""

mode = 6

import random


def player(sweets, count):
    print('Oсталось {} конфет'.format(sweets))
    num = int(input('{} игрок '.format(count % 2 + 1)))
    while num > 28 or num > sweets:
        print('ввели не верное колличество')
        num = int(input('{} игрок '.format(count % 2 + 1)))
    sweets -= num
    return sweets


def game(sweets, count, player1, player2):
    while sweets != 0:
        count += 1
        if count % 2 == 0:
            sweets = player1(sweets, count)
        else:
            sweets = player2(sweets, count)
    print('Выйграл {} игрок'.format(count % 2 + 1))


def monetka():
    a = random.randint(0, 1)
    return a


def bot_easy(sweets, count):
    print('Oсталось {} конфет'.format(sweets))
    a = 28
    if a > sweets:
        a = sweets
    b = random.randint(1, a)
    print('Бот {} взял {} конфет'.format(count % 2 + 1, b))
    sweets -= b
    return sweets


def bot_expert(sweets, count):
    print('Oсталось {} конфет'.format(sweets))
    a = sweets % 28 - 1
    if a == -1:
        a = 1
    if 28 >= sweets:
        a = sweets
    print('Бот {} взял {} конфет'.format(count % 2 + 1, a))
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
    print('Вы указали не правильный режим игры, можно изменить в начале программы')

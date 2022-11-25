from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/sum\n/calc\n/help')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    my_str = update.message.text[5:]

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

    def run(my_list: list):
        tmp_list = my_list.copy()
        idx = 0
        while idx < len(tmp_list):
            elem = tmp_list[idx]
            if elem == '*':
                tmp_list[idx - 1] *= tmp_list[idx + 1]
                tmp_list.pop(idx)
                tmp_list.pop(idx)
                idx -= 1
            elif elem == '/':
                tmp_list[idx - 1] /= tmp_list[idx + 1]
                tmp_list.pop(idx)
                tmp_list.pop(idx)
                idx -= 1
            idx += 1
        idx = 0
        while idx < len(tmp_list):
            elem = tmp_list[idx]
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
            idx += 1
        return tmp_list[0]
    update.message.reply_text(run(pars_str(my_str)))
import os
import re
import random
from dataclasses import dataclass

import telebot

import constants


bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_API_KEY')
)


@dataclass
class Message:
    amount: float
    category: str


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, constants.START_TEXT)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, constants.COMMANDS)


@bot.message_handler(commands=['today'])
def today(message):
    pass


@bot.message_handler(commands=['week'])
def week(message):
    pass


@bot.message_handler(commands=['month'])
def month(message):
    pass


@bot.message_handler(commands=['status'])
def status(message):
    pass


@bot.message_handler(commands=['categories'])
def categories(message):
    bot.send_message(message.chat.id, ', '.join(constants.CATEGORIES.keys()))


@bot.message_handler(commands=['share'])
def share(message):
    pass


@bot.message_handler(func=lambda message: True)
def text(message):
    result = parse_message(message)
    answer = random_answer() if result else "I don't understand you("
    bot.send_message(message.chat.id, answer)


def parse_message(message):
    match = re.match(constants.AMOUNT_CATEGORY_REGEXP, message.text)

    return Message(
        amount=match.group(1).replace('$', ''), category=match.group(2)
    ) if match else None


def random_answer():
    return random.choice(constants.ANSWERS)


if __name__ == '__main__':
    bot.polling()

import os
import re
import random
import datetime
from dataclasses import dataclass

import telebot

import constants
from models import create_tables, User, Expense


bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_API_KEY')
)


@dataclass
class Message:
    amount: float
    category: str


@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username

    if not User.get_or_none(User.username == username):
        User.create(username=username)

    bot.send_message(message.chat.id, constants.START_TEXT)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, constants.COMMANDS)


@bot.message_handler(commands=['today'])
def today(message):
    spent = Expense.objects.today()
    bot.send_message(message.chat.id, f"You spent today {spent}$")


@bot.message_handler(commands=['week'])
def week(message):
    spent = Expense.objects.week()
    bot.send_message(message.chat.id, f"You spent in this week {spent}$")


@bot.message_handler(commands=['month'])
def month(message):
    spent = Expense.objects.month()
    bot.send_message(message.chat.id, f"You spent in this month {spent}$")


@bot.message_handler(commands=['status'])
def status(message):
    spents = "\n".join(
        [
            f"  {record.category}: {record.total}$"
            for record in Expense.objects.status()
        ]
    )
    bot.send_message(message.chat.id, f"You spent by categories: \n{spents}")


@bot.message_handler(commands=['categories'])
def categories(message):
    bot.send_message(message.chat.id, ', '.join(constants.CATEGORIES.keys()))


@bot.message_handler(commands=['share'])
def share(message):
    if not message.text.startwith('@'):
        bot.send_message(message.chat.id, "Send message with: @username")
    username = message.text.replace('@', '')
    # TODO: Added in Share model
    bot.send_message(message.chat.id, f"Shared with the user {username}")


@bot.message_handler(func=lambda message: True)
def text(message):
    result = parse_message(message)
    if result:
        Expense.create(
            amount=result.amount,
            category=result.category,
            user=User.get(User.username == message.from_user.username)
        )
    answer = random_answer() if result else "I don't understand you("
    bot.send_message(message.chat.id, answer)


def parse_message(message):
    match = re.match(constants.AMOUNT_CATEGORY_REGEXP, message.text)

    return Message(
        amount=match.group(1).replace('$', ''),
        category=match_category(match.group(2))
    ) if match else None


def random_answer():
    return random.choice(constants.ANSWERS)


def match_category(category):
    if category in constants.CATEGORIES.keys():
        return category

    for key in constants.CATEGORIES:
        if category in constants.CATEGORIES.get(key):
            return key

    return constants.DEFAULT_CATEGORY


if __name__ == '__main__':
    create_tables()
    bot.polling()

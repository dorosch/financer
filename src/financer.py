import re
import random
from dataclasses import dataclass

import constants
from settings import bot
from models import User, Expense


@dataclass
class Message:
    amount: float
    category: str


@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Process command '/start' for a new user
    """
    # Save a new user
    User.get_or_create(username=message.from_user.username)

    # Send welcome text
    bot.send_message(message.chat.id, constants.WELCOME_TEXT)


@bot.message_handler(commands=['help'])
def handle_help(message):
    """
    Send help about available commands.
    """
    bot.send_message(message.chat.id, constants.COMMANDS)


@bot.message_handler(commands=['today'])
def handle_today(message):
    """
    Calculate spending today.
    """
    answer = f"You spent today {Expense.objects.today()}$"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['week'])
def handle_week(message):
    """
    Calculate spending per week.
    """
    answer = f"You spent in this week {Expense.objects.week()}$"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['month'])
def handle_month(message):
    """
    Calculate spending per month.
    """
    spent = Expense.objects.month()
    bot.send_message(message.chat.id, f"You spent in this month {spent}$")


@bot.message_handler(commands=['status'])
def handle_status(message):
    """
    Calculate spending by category for the last month.
    """
    spents = "\n".join(
        [
            f"  {record.category}: {round(record.total, 2)}$"
            for record in Expense.objects.status()
        ]
    )
    bot.send_message(message.chat.id, f"You spent by categories: \n{spents}")


@bot.message_handler(commands=['categories'])
def handle_categories(message):
    """
    Return Available Categories.
    """
    bot.send_message(message.chat.id, ', '.join(constants.CATEGORIES.keys()))


@bot.message_handler(commands=['share'])
def handle_share(message):
    # TODO: Implement me!
    bot.send_message(message.chat.id, "Not implemented yet, sorry")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    """
    Process message like: '1.5$ coffee'
    """
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
    bot.polling()

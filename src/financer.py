import os

import telebot


bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_API_KEY')
)


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()

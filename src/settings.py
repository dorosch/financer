import os

import telebot
import peewee as models


bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_API_KEY')
)

USE_FULL_SYNC_ON_DISK = 3

USE_FILE_AS_STORAGE_DB = 1

DATABASE = models.SqliteDatabase('database.db', pragmas={
    'journal_mode': 'wal',
    'checkpoint_fullfsync': True,
    'synchronous': USE_FULL_SYNC_ON_DISK,
    'temp_store': USE_FILE_AS_STORAGE_DB
})

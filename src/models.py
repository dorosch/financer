import datetime

import peewee as models

import constants


db = models.SqliteDatabase('database.sqlite')


class User(models.Model):
    username = models.CharField(
        unique=True
    )


class Expense(models.Model):
    user = models.ForeignKeyField(
        User,
        backref='expenses'
    )

    amount = models.FloatField(
        default=0
    )

    category = models.CharField(
        choices=[
            (category, category.capitalize())
            for category in constants.CATEGORIES.keys()
        ]
    )

    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )

    class Meta:
        database = db

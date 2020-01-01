import datetime

import peewee as models

import constants
import querysets


db = models.SqliteDatabase('database.sqlite')


class User(models.Model):
    username = models.CharField(
        unique=True
    )

    objects = querysets.UserQueryset()

    class Meta:
        database = db


class Share(models.Model):
    user = models.ForeignKeyField(
        User
    )

    participant = models.ForeignKeyField(
        User,
        backref='shared'
    )

    objects = querysets.ShareQueryset()

    class Meta:
        database = db


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

    objects = querysets.ExpenseQueryset()

    class Meta:
        database = db


def create_tables():
    with db as database:
        database.create_tables([User, Share, Expense])

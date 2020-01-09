import datetime

import peewee as models

import constants
import querysets
import settings


class User(models.Model):
    username = models.CharField(
        unique=True
    )

    objects = querysets.UserQueryset()

    class Meta:
        database = settings.DATABASE


class Share(models.Model):
    user = models.ForeignKeyField(
        User
    )
    participant = models.ForeignKeyField(
        User, backref='shared'
    )

    objects = querysets.ShareQueryset()

    class Meta:
        database = settings.DATABASE


class Expense(models.Model):
    user = models.ForeignKeyField(
        User, backref='expenses'
    )
    amount = models.FloatField(
        default=0
    )
    category = models.CharField(
        choices=constants.CATEGORIES_CHOICES
    )
    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )

    objects = querysets.ExpenseQueryset()

    class Meta:
        database = settings.DATABASE


with settings.DATABASE as database:
    database.create_tables([User, Share, Expense])

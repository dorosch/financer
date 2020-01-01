import datetime

from peewee import fn

import models


class UserQueryset:
    pass


class ShareQueryset:
    pass


class ExpenseQueryset:
    @staticmethod
    def _total_amount():
        return models.Expense.select(
            fn.SUM(models.Expense.amount).alias('total')
        )

    def today(self):
        now = datetime.datetime.now()
        return self._total_amount().where(
            (models.Expense.created_at.year == now.year) &
            (models.Expense.created_at.month == now.month) &
            (models.Expense.created_at.day == now.day)
        ).first().total or 0

    def week(self):
        now = datetime.datetime.now()
        week_ago = now - datetime.timedelta(days=7)
        return self._total_amount().where(
            models.Expense.created_at >= week_ago
        ).first().total or 0

    def month(self):
        now = datetime.datetime.now()
        return self._total_amount().where(
            (models.Expense.created_at.year == now.year) &
            (models.Expense.created_at.month == now.month)
        ).first().total or 0

    @staticmethod
    def status():
        return models.Expense.select(
            models.Expense.category,
            fn.SUM(models.Expense.amount).alias('total')
        ).group_by(
            models.Expense.category
        )

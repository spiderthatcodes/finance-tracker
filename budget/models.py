from django.db import models


class Bill(models.Model):
    company = models.CharField(max_length=200)
    due_date = models.DateField()
    balance = models.BigIntegerField(null=True)
    amount = models.BigIntegerField()


class LineItem(models.Model):
    title = models.CharField(max_length=250)
    savings = models.BooleanField(default=False)
    amount_to_pay = models.BigIntegerField()
    bill = models.ForeignKey(
        'Bill',
        related_name='line_items',
        on_delete=models.CASCADE
    )


class Paychecks(models.Model):
    line_item = models.ForeignKey(
        'LineItem',
        related_name='paychecks',
        on_delete=models.CASCADE
    )


class Savings(models.Model):
    balance = models.BigIntegerField()

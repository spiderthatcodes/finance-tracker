from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Bill, LineItem, Paychecks, Savings


class BillEncoder(ModelEncoder):
    model = Bill
    properties = ['id','company', 'due_date', 'balance', 'amount']


class LineItem(ModelEncoder):
    model = LineItem
    properties = ['title', 'savings', 'amount_to_pay', 'bill']

    encoders = {
        'bill': BillEncoder()
    }

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Bill, LineItem, Paychecks, Savings


class BillEncoder(ModelEncoder):
    model = Bill
    properties = ['id','company', 'due_date', 'balance', 'amount']


class LineItemEncoder(ModelEncoder):
    model = LineItem
    properties = ['title', 'savings', 'amount_to_pay', 'bill']

    encoders = {
        'bill': BillEncoder()
    }


class PaychecksEncoder(ModelEncoder):
    model = Paychecks
    properties = ['date', 'check_amount', 'line_item']
    encoders = {
        'line_item': LineItemEncoder()
    }


class SavingsEncoder(ModelEncoder):
    model = Savings
    properties = ['balance']


@require_http_methods(["GET", "POST"])
def get_or_create_bill(request):
    if request.method == 'GET':
        bills = Bill.objects.all()
        return JsonResponse(
            {'bills': bills},
            encoder=BillEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        bill = Bill.objects.create(**content)
        return JsonResponse(
            bill,
            encoder=BillEncoder,
            safe=False
        )

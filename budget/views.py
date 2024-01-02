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
    properties = ['id', 'title', 'savings', 'amount_to_pay', 'bill']

    encoders = {
        'bill': BillEncoder()
    }


class PaychecksEncoder(ModelEncoder):
    model = Paychecks
    properties = ['id', 'date', 'check_amount', 'line_item']
    encoders = {
        'line_item': LineItemEncoder()
    }


class SavingsEncoder(ModelEncoder):
    model = Savings
    properties = ['id', 'balance']


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


@require_http_methods(["GET", "PUT", "DELETE"])
def other_bill_actions(request, id):
    if request.method == 'GET':
        bill = Bill.objects.get(id=id)
        return JsonResponse(
            bill,
            encoder=BillEncoder
        )
    elif request.method == "DELETE":
        count, _ = Bill.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        try:
            bill = Bill.objects.filter(id=id).update(**content)
            return JsonResponse(
                bill,
                encoder=BillEncoder,
                safe=False
            )
        except Bill.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bill id"},
                status=400
            )


@require_http_methods(["GET", "POST"])
def get_or_create_paycheck(request):
    if request.method == 'GET':
        paychecks = Paychecks.objects.all()
        return JsonResponse(
            {'paychecks': paychecks},
            encoder=PaychecksEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        paycheck = Paychecks.objects.create(**content)
        return JsonResponse(
            paycheck,
            encoder=PaychecksEncoder,
            safe=False
        )

from django.contrib import admin
from .models import Bill, LineItem, Paychecks, Savings


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'amount'
    )


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'amount_to_pay'
    )


@admin.register(Savings)
class LineItemAdmin(admin.ModelAdmin):
    list_display = (
        'balance',
    )

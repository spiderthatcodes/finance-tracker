# Generated by Django 4.0.3 on 2023-12-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_paychecks_check_amount_paychecks_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='budget.bill'),
        ),
    ]

# Generated by Django 5.1.4 on 2025-02-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_fundpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundpayment',
            name='amount',
            field=models.IntegerField(),
        ),
    ]

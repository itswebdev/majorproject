# Generated by Django 5.1.4 on 2025-01-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_campneeds_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]

# Generated by Django 5.1.4 on 2025-02-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_volunteerrequest_totalallocated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerrequest',
            name='totalallocated',
            field=models.IntegerField(default=0),
        ),
    ]

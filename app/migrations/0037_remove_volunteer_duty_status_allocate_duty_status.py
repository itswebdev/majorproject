# Generated by Django 5.1.4 on 2025-02-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_volunteer_duty_status_alter_duty_duty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='duty_status',
        ),
        migrations.AddField(
            model_name='allocate',
            name='duty_status',
            field=models.CharField(default='Not Scheduled', max_length=100),
        ),
    ]

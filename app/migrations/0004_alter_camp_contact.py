# Generated by Django 5.1.4 on 2025-01-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_camp_login_id_alter_camp_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]

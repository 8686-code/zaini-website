# Generated by Django 4.2.3 on 2023-07-29 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_alter_contact_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 16, 47, 22, 853141, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-25 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_remove_contact_timestamp_contact_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 23, 8, 17, 834526, tzinfo=datetime.timezone.utc)),
        ),
    ]

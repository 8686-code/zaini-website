# Generated by Django 4.2.3 on 2023-07-30 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0014_alter_contact_date_time_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 30, 22, 52, 54, 649982, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

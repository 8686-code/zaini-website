# Generated by Django 4.2.3 on 2023-07-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Mobile_Number', models.IntegerField()),
                ('State', models.CharField(max_length=256)),
                ('Required_Part', models.CharField(max_length=256)),
                ('Make', models.CharField(max_length=256)),
                ('Model', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]

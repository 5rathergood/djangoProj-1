# Generated by Django 3.2.5 on 2022-02-21 07:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestDB',
            fields=[
                ('click_date', models.DateTimeField(default=datetime.datetime(2022, 2, 21, 7, 38, 58, 305327, tzinfo=utc), primary_key=True, serialize=False)),
                ('n_click', models.IntegerField(default=-1)),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2022-05-04 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0004_auto_20220504_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='count_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 2, 44, 16, 518492), null=True),
        ),
        migrations.AlterField(
            model_name='todayrecord',
            name='count_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 2, 44, 16, 517487)),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-09 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20200309_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 13, 50, 31, 996208, tzinfo=utc)),
        ),
    ]

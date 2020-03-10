# Generated by Django 3.0.4 on 2020-03-09 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2020, 3, 9, 13, 47, 43, 471322, tzinfo=utc))),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-11-26 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20201126_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 14, 43, 50, 38296, tzinfo=utc)),
        ),
    ]

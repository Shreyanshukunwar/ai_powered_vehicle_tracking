# Generated by Django 3.0.8 on 2020-11-26 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20201126_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

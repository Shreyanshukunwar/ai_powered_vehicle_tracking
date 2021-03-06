# Generated by Django 3.0.8 on 2020-11-26 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_map_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingVehicle',
            fields=[
                ('missingVehicle_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_id', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('licensenumber', models.CharField(default='', max_length=60)),
                ('location', models.CharField(default='', max_length=60)),
                ('field_name', models.TimeField(auto_now=True)),
            ],
        ),
    ]

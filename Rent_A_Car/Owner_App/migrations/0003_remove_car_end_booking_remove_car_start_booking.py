# Generated by Django 5.0.2 on 2024-02-24 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_App', '0002_car_end_booking_car_out_of_service_car_start_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='end_booking',
        ),
        migrations.RemoveField(
            model_name='car',
            name='start_booking',
        ),
    ]

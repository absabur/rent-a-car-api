# Generated by Django 5.0.2 on 2024-02-24 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client_App', '0003_booking_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_at']},
        ),
    ]

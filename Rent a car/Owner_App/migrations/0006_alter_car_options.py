# Generated by Django 5.0.2 on 2024-02-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_App', '0005_alter_car_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['out_of_service', '-updated_at', '-created_at']},
        ),
    ]
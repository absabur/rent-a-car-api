# Generated by Django 5.0.2 on 2024-02-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(),
        ),
    ]

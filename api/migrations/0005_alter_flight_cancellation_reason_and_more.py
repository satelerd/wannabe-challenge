# Generated by Django 4.0.2 on 2022-11-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_flight_cancellation_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='cancellation_reason',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination_airport',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin_airport',
            field=models.CharField(default='', max_length=100),
        ),
    ]

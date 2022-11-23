# Generated by Django 4.0.2 on 2022-11-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(max_length=3)),
                ('airline', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='airline',
            new_name='airport',
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='airport',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='airport',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='airport',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]

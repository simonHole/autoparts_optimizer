# Generated by Django 4.1.5 on 2023-01-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_engine_power_alter_car_end_production'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='fuel_type',
            field=models.CharField(choices=[('d', 'Diesel Engine'), ('g', 'Gas Engine')], max_length=1, null=True),
        ),
    ]
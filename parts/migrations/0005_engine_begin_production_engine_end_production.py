# Generated by Django 4.1.5 on 2023-01-16 20:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_engine_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='begin_production',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1953), django.core.validators.MaxValueValidator(2023)]),
        ),
        migrations.AddField(
            model_name='engine',
            name='end_production',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1953), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-22 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0006_alter_part_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='is_original',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='quality_fac',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
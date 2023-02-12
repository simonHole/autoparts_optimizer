# Generated by Django 4.1.5 on 2023-01-29 17:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_alter_part_is_original_alter_part_quality_fac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='price',
            field=models.FloatField(default=0, null=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='part',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parts.vendor'),
        ),
    ]
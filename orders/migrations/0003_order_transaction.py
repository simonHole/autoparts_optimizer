# Generated by Django 4.1.5 on 2023-01-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_part_order_client_order_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

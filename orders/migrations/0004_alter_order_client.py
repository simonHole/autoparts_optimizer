# Generated by Django 4.1.5 on 2023-02-09 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_client_location'),
        ('orders', '0003_order_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client'),
        ),
    ]

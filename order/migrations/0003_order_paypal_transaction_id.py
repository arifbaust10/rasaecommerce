# Generated by Django 5.0.6 on 2024-08-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_addresh_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paypal_transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
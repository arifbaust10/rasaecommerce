# Generated by Django 5.0.6 on 2024-08-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_paypal_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('On the way', 'On the way'), ('Delivered', 'Delivered')], default='Recieved', max_length=15),
        ),
    ]

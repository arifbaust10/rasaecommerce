# Generated by Django 5.0.6 on 2024-08-02 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_coupon_required_amount_to_use_coupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='required_amount_to_use_coupo',
            new_name='required_amount_to_use_coupon',
        ),
    ]

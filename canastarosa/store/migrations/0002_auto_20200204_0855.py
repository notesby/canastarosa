# Generated by Django 3.0.3 on 2020-02-04 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='build_days',
            new_name='elaboration_time',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='total',
            new_name='order_price',
        ),
        migrations.RenameField(
            model_name='storeschedule',
            old_name='end',
            new_name='closes',
        ),
        migrations.RenameField(
            model_name='storeschedule',
            old_name='start',
            new_name='opens',
        ),
    ]

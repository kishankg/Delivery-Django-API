# Generated by Django 3.1.5 on 2021-01-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivered_order',
            name='delivery_address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='pending_order',
            name='delivery_address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='pending_order',
            name='delivery_status_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pending_order',
            name='slot_number',
            field=models.IntegerField(),
        ),
    ]

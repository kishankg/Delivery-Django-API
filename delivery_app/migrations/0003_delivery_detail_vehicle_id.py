# Generated by Django 3.1.5 on 2021-01-22 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0002_auto_20210118_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_detail',
            name='vehicle_id',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='delivery_app.vehicle_detail'),
        ),
    ]

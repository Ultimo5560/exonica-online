# Generated by Django 3.2.6 on 2022-01-15 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_exonica', '0023_auto_20220114_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='instalacion',
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='instalacion',
            field=models.BooleanField(default=False),
        ),
    ]

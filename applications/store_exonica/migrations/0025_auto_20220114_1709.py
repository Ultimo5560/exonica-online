# Generated by Django 3.2.6 on 2022-01-15 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_exonica', '0024_auto_20220114_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='costo_instalacion',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Instalación'),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='instalacion',
            field=models.BooleanField(),
        ),
    ]

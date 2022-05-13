# Generated by Django 3.2.6 on 2022-01-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_exonica', '0020_alter_carshop_instalacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='envio',
        ),
        migrations.AddField(
            model_name='payment',
            name='costo_instalacion',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=10, verbose_name='Instalación'),
        ),
        migrations.AddField(
            model_name='payment',
            name='instalacion',
            field=models.BooleanField(default=False),
        ),
    ]

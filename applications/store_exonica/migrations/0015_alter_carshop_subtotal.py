# Generated by Django 3.2.6 on 2022-01-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_exonica', '0014_carshop_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshop',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal'),
        ),
    ]

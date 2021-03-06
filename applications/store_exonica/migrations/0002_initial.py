# Generated by Django 3.2.6 on 2022-01-03 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_exonica', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_exonica', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carshop',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_car', to='admin_exonica.articulos', verbose_name='producto'),
        ),
        migrations.AddField(
            model_name='carshop',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_carshop', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.6 on 2022-03-01 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exonica', '0009_alter_articulos_precio_inst_fuera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncios',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

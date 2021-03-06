# Generated by Django 3.2.6 on 2022-01-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('celular', models.CharField(blank=True, default=False, max_length=10)),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default=False, max_length=10)),
                ('ciudad', models.CharField(blank=True, default=False, max_length=20)),
                ('estado', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default=False, max_length=20)),
                ('direccion_envio', models.CharField(blank=True, default=False, max_length=100, verbose_name='Direccion de envío')),
                ('ocupations', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Cliente', 'Cliente')], default='Cliente', max_length=15)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super Usuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

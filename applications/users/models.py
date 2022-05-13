from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    ADMINISTRADOR = 'Administrador'
    CLIENTE = 'Cliente'

    HOMBRE = 'Masculino'
    MUJER = 'Femenino'

    AGUAS_CALIENTE = 'Aguascalientes'
    BAJA_CALIFORNIA = 'Baja California'
    BAJA_CALIFORNIA_SUR = 'Baja California Sur'
    CAMPECHE = 'Campeche'
    CHIAPAS = 'Chiapas'
    CHIHUAHUA = 'Chihuahua'
    COAHUILA = 'Coahuila'
    COLIMA = 'Colima'
    DURANGO = 'Durango'
    GUANAJUATO = 'Guanajuato'
    GUERRERO = 'Guerrero'
    HIDALGO = 'Hidalgo'
    JALISCO = 'Jalisco'
    EDO_MEXICO = 'Estado de México'
    MICHOACAN = 'Michoacán'
    MORELOS = 'Morelos'
    NAYARIT = 'Nayarit'
    NUEVO_LEON = 'Nuevo León'
    OAXACA = 'Oaxaca'
    PUEBLA = 'Puebla'
    QUERETARO = 'Querétaro'
    QUINTANA_ROO = 'Quintana Roo'
    SAN_LUIS_PTSI = 'San Luis Potosí'
    SINALOA = 'Sinaloa'
    SONORA = 'Sonora'
    TABASCO = 'Tabasco'
    TAMAULIPAS = 'Tamaulipas'
    TLAXCALA = 'Tlaxcala'
    VERACRUZ = 'Veracruz'
    YUCATAN = 'Yucatán'
    ZACATECAS = 'Zacatecas'



    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (CLIENTE, 'Cliente'),
    ]


    GENERO_CHOICES = [
        (HOMBRE, 'Masculino'),
        (MUJER, 'Femenino'),
    ]
        
    

    STATE_CHOICES = [
        (AGUAS_CALIENTE, 'Aguascalientes'),
        (BAJA_CALIFORNIA, 'Baja California'),
        (BAJA_CALIFORNIA_SUR, 'Baja California Sur'),
        (CAMPECHE, 'Campeche'),
        (CHIAPAS, 'Chiapas'),
        (CHIHUAHUA, 'Chihuahua'),
        (COAHUILA, 'Coahuila'),
        (COLIMA, 'Colima'),
        (DURANGO, 'Durango'),
        (GUANAJUATO, 'Guanajuato'),
        (GUERRERO, 'Guerrero'),
        (HIDALGO, 'Hidalgo'),
        (JALISCO, 'Jalisco'),
        (EDO_MEXICO, 'Estado de México'),
        (MICHOACAN, 'Michoacán'),
        (MORELOS, 'Morelos'),
        (NAYARIT, 'Nayarit'),
        (NUEVO_LEON, 'Nuevo León'),
        (OAXACA, 'Oaxaca'),
        (PUEBLA, 'Puebla'),
        (QUERETARO, 'Querétaro'),
        (QUINTANA_ROO, 'Quintana Roo'),
        (SAN_LUIS_PTSI, 'San Luis Potosí'),
        (SINALOA, 'Sinaloa'),
        (SONORA, 'Sonora'),
        (TABASCO, 'Tabasco'),
        (TAMAULIPAS, 'Tamaulipas'),
        (TLAXCALA, 'Tlaxcala'),
        (VERACRUZ, 'Veracruz'),
        (YUCATAN, 'Yucatán'),
        (ZACATECAS, 'Zacatecas')
    ]

    nombre = models.CharField(max_length=20, blank=False)
    apellidos = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=10)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    ciudad = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=STATE_CHOICES)
    direccion_envio = models.CharField('Direccion de envío', max_length=100)
    cpostal = models.CharField('Codigo Postal', max_length=6)
    ocupations = models.CharField(max_length=15, choices=OCUPATION_CHOICES, default=CLIENTE)

    # administrador o no
    is_staff = models.BooleanField(default=False)
    # super usuario o no
    is_superuser = models.BooleanField('Super Usuario', default=False)
    
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_short_name(self):
        return self.nombre
    def get_full_name(self):
        return self.nombre + ' ' + self.apellidos

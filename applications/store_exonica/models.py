from django.db import models
from django.db.models.fields import BooleanField
from applications.admin_exonica.managers import ContactManager, PaymentManager
from applications.admin_exonica.models import Articulos
from .managers import CarShopManager
from django.conf import settings
from django.db.models.signals import post_save
from PIL import Image
# app_terceros
from model_utils.models import TimeStampedModel

class FormContact(TimeStampedModel):
    """Formulario de contacto"""
    full_name = models.CharField(
        'Nombres', 
        max_length=60
    )
    email = models.EmailField()
    celphone= models.CharField(
        'Celular',
        blank=True,
        max_length=10
    )
    message = models.TextField(
        'Mensaje',
        max_length=200
    )
    read = models.BooleanField(default=False)

    objects = ContactManager()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name

class CarShop(TimeStampedModel):
    """Modelo que representa a un carrito de compras"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_carshop',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Articulos,
        on_delete=models.CASCADE,
        verbose_name='producto',
        related_name='product_car'
    )
    subtotal = models.DecimalField(
        'Subtotal', 
        max_digits=10, 
        decimal_places=2,
    )
    instalacion = models.BooleanField()
    count = models.PositiveIntegerField('Cantidad')
    
    objects = CarShopManager()

    class Meta:
        verbose_name = 'Carrito de compras'
        verbose_name_plural = 'Carrito de compras'
        ordering = ['-created']

    def __str__(self):
        return str(self.product.title)

class Payment(TimeStampedModel):
    VERYFY = 'VERIFICANDO DATOS'
    ORDERED = 'EN PROCESO DE ENVIO'
    SHIPPED = 'EN CAMINO'
    ARRIVED = 'ENTREGADO'

    PAYPAL = 'PayPal'
    TRANSFERENCIA = 'Transferencia'

    STATUS_CHOICES = (
        (VERYFY, 'VERIFICANDO DATOS'),
        (ORDERED, 'EN PROCESO DE ENVIO'),
        (SHIPPED, 'EN CAMINO'),
        (ARRIVED, 'ENTREGADO')
    )
    STATUS_CHOICES2 = (
        (PAYPAL, 'PayPal'),
        (TRANSFERENCIA, 'Transferencia'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_payment',
        on_delete=models.CASCADE,
    )
    payment_method = models.CharField(max_length=20, choices=STATUS_CHOICES2)
    comprobante_pago = models.ImageField(
        'Comprobante de pago',
        upload_to='comprobantes_de_pago',
        height_field=None,
        width_field=None,
        max_length=None,
        null=True
    )
    amount = models.FloatField()
    succesful = BooleanField()
    raw_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    objects = PaymentManager()

    class Meta:
        verbose_name = 'Payment'
        ordering = ['-created']


    def delete(self, *args, **kwargs):
        if self.payment_method == 'Transferencia':
            # recuras la ruta del archivo en el disco
            storage, path = self.comprobante_pago.storage, self.comprobante_pago.path
            # se ejecuta el metodo delete del modelo
            super(Payment, self).delete(*args, **kwargs)
            # una vez eliminado limpias el archivo de disco
            storage.delete(path)
        else:
            super(Payment, self).delete(*args, **kwargs)

def optimize_image(sender, instance, **kwargs):
    print("------------------------")
    if instance.comprobante_pago:
        comprobante_pago = Image.open(instance.comprobante_pago.path)
        comprobante_pago.save(instance.comprobante_pago.path, quality=70, optimize=True)

post_save.connect(optimize_image, sender=Payment)


class PaymentDetail(TimeStampedModel):
    """Modelo que representa a una venta en detalle"""

    product = models.ForeignKey(
        Articulos,
        on_delete=models.CASCADE,
        verbose_name='producto',
        related_name='product_sale'
    )
    sale = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE, 
        related_name='detail_payment'
    )
    count = models.PositiveIntegerField('Cantidad')
    price_sale = models.DecimalField(
        'Precio Venta', 
        max_digits=10, 
        decimal_places=2
    )
    instalacion = models.BooleanField()
    costo_instalacion = models.DecimalField(
        'Instalación', 
        max_digits=10, 
        decimal_places=2,
    )
    #

    objects = CarShopManager()

    class Meta:
        verbose_name = 'Producto Vendido'
        verbose_name_plural = 'Productos vendidos'

    def __str__(self):
        return str(self.sale.id) + ' - ' + str(self.product.title)


class AboutExonica(TimeStampedModel):
    """modelo para datos en pantalla home"""
    qsomos = models.TextField(
        'Quienes somos', 
        max_length=500
    )


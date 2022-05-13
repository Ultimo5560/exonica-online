from django.db import models
# python
from django.db.models.fields import IntegerField
# django
from django.db import models
#


from django.db.models import Q, Sum, F, FloatField
from django.views.generic.base import View

class CarShopManager(models.Manager):
    """ procedimiento modelo Carrito de compras """
    
    def total_cobrar(self, usuario):
        
        consulta = self.filter(
            user = usuario
        ).aggregate(
            total=Sum(
                F('subtotal'),
                output_field=FloatField()
            ),
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0 

    def entradas_user(self, usuario):
        return self.filter(
            product__public=True,
            user=usuario
        ).order_by('-created')

    def entradas_payment(self, usuario):
        consulta = self.filter(
            order__product__public=True,
            user=usuario
        )
        return consulta

    def num_car(self, usuario):
        
        consulta = self.filter(
            user = usuario
        ).aggregate(
            total=Sum(
                F('count'),
                output_field=IntegerField()
            ),
        )
        if consulta['total']:
            return consulta
        else:
            return 0

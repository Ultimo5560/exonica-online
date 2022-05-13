from django.db import models
from django.db.models import Q


class EntryManager(models.Manager):
    """Procedimiento para las entradas de anuncios y articulos"""
 
    def anuncios_en_portada(self):
        # Devuelve los anuncios para la portada en home
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created')

    def articulos_en_home(self):
        # Devuelve los primeros 12 articulos en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-title')[:16]

    def articulos_recientes(self):
        # Devuelve las ultimas 6 entradas de articulos
        return self.filter(
            public=True,
        ).order_by('-created')[:6]

    def buscar_articulos(self, kword, categoria):
        # procedimiento para buscar articulos por palabra clave o categorias
        if len(categoria) > 0:
            return self.filter(
                categoria__short_name = categoria,
                title__icontains = kword,
                public=True,
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains = kword,
                public=True,
            ).order_by('-created')



class PaymentManager(models.Manager):
    def buscar_pedido(self, categoria):
        # procedimiento para buscar articulos por palabra clave o categorias
        return self.filter(
            status = categoria,
        ).order_by('-created')

    def user_last(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')[:1]

    def user_five_last(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')[:5]

    def compras_num(self):
        return self.filter(
            Q(status='VERIFICANDO DATOS') | Q(status='EN PROCESO DE ENVIO')
        ).count()



class ContactManager(models.Manager):
    def num_msj(self):
        return self.filter(
            read=False,
        ).count()



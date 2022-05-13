from django.db import models
from django.conf import settings
from applications.admin_exonica.models import Articulos
# app_terceros
from model_utils.models import TimeStampedModel
    

# Create your models here.

class Favorites(TimeStampedModel):
    """modelo para favoritos"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    articulos = models.ForeignKey(
        Articulos,
        related_name='articulos_favoritos',
        on_delete=models.CASCADE
    )

    class Meta:
        """unique_together no permite que se repita el articulo en un ususario"""
        unique_together=('user', 'articulos')
        verbose_name='Articulo favorito'
        verbose_name_plural='Articulos favoritos'

    def __str__(self):
        return self.articulos.title
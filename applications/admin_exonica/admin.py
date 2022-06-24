from django.contrib import admin

from .models import Anuncios, Articulos, CategoriaArticulos
from applications.store_exonica.models import AboutExonica
# Register your models here.

admin.site.register(CategoriaArticulos)
admin.site.register(Articulos)
admin.site.register(Anuncios)

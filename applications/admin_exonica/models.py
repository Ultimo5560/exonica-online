from datetime import timedelta, datetime
from django.db.models.fields import TextField
from django.template.defaultfilters import slugify
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy
from .managers import EntryManager
# app_terceros
from model_utils.models import TimeStampedModel
from PIL import Image

# Create your models here.

class CategoriaArticulos(TimeStampedModel):
    """Categoria de un articulo"""
    short_name = models.CharField(
        'Nombre corto', 
        max_length=15
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.name


class Articulos(TimeStampedModel):

    user = models.CharField(
        'usuario',
        max_length=30
    )

    title = models.CharField(
        'Titulo',
        max_length=30
    )
    precio = models.DecimalField(
        'precio compra',
        max_digits=7, 
        decimal_places=0
    )
    precio_inst = models.DecimalField(
        'Precio de la instalación en sonora',
        max_digits=7, 
        decimal_places=0,
    )
    precio_inst_fuera = models.DecimalField(
        'Precio de la instalación fuera de sonora',
        max_digits=7, 
        decimal_places=0,
    )
    descripcion = TextField(
        'Descripción'
    )
    categoria = models.ForeignKey(
        CategoriaArticulos,
        on_delete=models.CASCADE,
        related_name='categoria_articulo'
    )
    public = models.BooleanField(default=False)
    imagen = models.ImageField(
        'Imagen',
        upload_to='articulo',
        height_field=None,
        width_field=None,
        max_length=None
    )
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):

        try:
            this = Articulos.objects.get(id=self.id)
            if this.imagen != self.imagen:
                this.imagen.delete()
        except: pass


        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)

        super(Articulos, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # recuras la ruta del archivo en el disco
        storage, path = self.imagen.storage, self.imagen.path
        # se ejecuta el metodo delete del modelo
        super(Articulos, self).delete(*args, **kwargs)
        # una vez eliminado limpias el archivo de disco
        storage.delete(path)

    def get_absolute_url(self):
        return reverse_lazy(
            'store_app:articulo_pub', kwargs={'slug': self.slug})

        

def optimize_image(sender, instance, **kwargs):
    print("------------------------")
    if instance.imagen:
        imagen = Image.open(instance.imagen.path)
        imagen.save(instance.imagen.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender=Articulos)


class Anuncios(TimeStampedModel):
    user = models.CharField(
        'usuario',
        max_length=30
    )

    title = models.CharField(
        'Titulo',
        max_length=30
    )
    mensaje = TextField(
        'Mensaje'
    )
    public = models.BooleanField(default=False)
    imagen = models.ImageField(
        'Imagen',
        upload_to='portada',
        height_field=None,
        width_field=None,
        max_length=None
    )
    portada = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name='Anuncio'
        verbose_name_plural='Anuncios'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # recuras la ruta del archivo en el disco
        storage, path = self.imagen.storage, self.imagen.path
        # se ejecuta el metodo delete del modelo
        super(Anuncios, self).delete(*args, **kwargs)
        # una vez eliminado limpias el archivo de disco
        storage.delete(path)

    def save(self, *args, **kwargs):
        try:
            this = Anuncios.objects.get(id=self.id)
            if this.imagen != self.imagen:
                this.imagen.delete()
        except: pass
        super(Anuncios, self).save(*args, **kwargs)

def optimize_image(sender, instance, **kwargs):
    print("------------------------")
    if instance.imagen:
        imagen = Image.open(instance.imagen.path)
        imagen.save(instance.imagen.path, quality=50, optimize=True)

post_save.connect(optimize_image, sender=Anuncios)
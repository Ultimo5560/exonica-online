import datetime
from queue import PriorityQueue
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
from applications.admin_exonica.models import Articulos


class articulosSitem(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Articulos.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created

class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)
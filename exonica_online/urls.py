"""exonica_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from applications.store_exonica.sitemap import (
    Sitemap,
    articulosSitem
)
urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.admin_exonica.urls')),
    re_path('', include('applications.store_exonica.urls')),
    re_path('', include('applications.users.urls')),
    # Url Ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

sitemaps = {
    'site':Sitemap(
        [
            'store_app:pub_articulos'
        ]
    ),
    'articulos': articulosSitem
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml',
        sitemap, 
        {'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]


urlpatterns = urlpatterns_main + urlpatterns_sitemap
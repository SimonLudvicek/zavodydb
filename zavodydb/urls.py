"""
URL configuration for zavodydb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Z vestavěného modulu django.contrib importuje aplikaci admin
from django.contrib import admin
# Z vestavěného modulu django.urls importuje funkce path a include
from django.urls import path, include
# Z vestavěného modulu django.views.generic importuje třídu RedirectView
from django.views.generic import RedirectView
# Z vestavěného modulu django.conf.urls.static importuje funkci static
from django.conf.urls.static import static
# Ze stejné složky importuje modul settings
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
path('kulturistika/', include('kulturistika.urls')),
 # Domovská stránka je přesměrována na úvodní stránku aplikace movies
 path('', RedirectView.as_view(url='kulturistika/')),
]

# Do seznamu urlpatterns přidává cestu k statickým souborům podle nastavení konstant v settings.py
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Do seznamu urlpatterns přidává cestu k uploadovaným souborům podle nastavení konstant settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

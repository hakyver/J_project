"""
URL configuration for J_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entradatexto.urls')),]
#entrada aqui es la ruta principal que te dirije a la aplicacion y lo que sigue son las rutas que salen de ella
#para que sirve el include?
#para incluir las rutas que se encuentran el el archivo urls de la app indicada
#para que sirve el admin? R= para la pagina de administrador que te proporciona django

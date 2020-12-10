"""sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from registro import views


urlpatterns = [
    
    #path('indec', views.indec, name='indec.html'),
    #path('otroejemplo', views.otroform, name='otroform.html'),
    path('admin/', admin.site.urls),
    path('inicio.html', views.inicio, name='inicio.html'),
    path('sesion.html', views.login, name='sesion.html'),
    path('cerrar.html', views.cerrar, name=""),
    path('pagar.html', views.pagar, name='pagar.html'),
    path('tienda.html', views.tienda, name='tienda.html'),
    #path('cuenta.html', views.cuenta, name='cuenta.html'),
    path('logout', views.cerrar),
    path('action_page.html', views.action, name='cuenta.html'),
    path('cuenta.html',views.registro_usuario, name='registro_usuario'),
    path('modificar/<id>/' , views.modificar_pedido, name='modificar_pedido'),
    path('PedidoMod.html', views.pedidoMod, name='PedidoMod.html'),
    path('eliminar/<id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

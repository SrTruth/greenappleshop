from django.contrib import admin


# Register your models here.
from .models import Pedido


class AdminPedido(admin.ModelAdmin):
    list_display=["email","direccion","rut","fechahora"]
    list_filter=["fechahora"]
    list_editable=["direccion"]

admin.site.register(Pedido,AdminPedido)

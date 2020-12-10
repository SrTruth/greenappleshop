from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#class Persona(models.Model):
   #nombre=models.CharField(max_length=25, blank=True, null=True)
    #email=models.EmailField()
    #fechahora=models.DateTimeField(auto_now=False,auto_now_add=True)


    #def __str__(self):
     #   return self.email

    #python 2
    #def __unicode__(self):
    #    return self.email
class Pedido(models.Model):
    direccion=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField()
    rut=models.CharField(max_length=12)
    fechahora=models.DateTimeField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.email


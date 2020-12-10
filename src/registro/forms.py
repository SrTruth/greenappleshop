from django import forms
from .models import Pedido
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

#from .models import Post


class RegistroModeloPedido(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=["direccion","rut","email"]

    def clean_nombre(self):
        nombre=self.cleaned_data.get("direccion")
        if len(nombre)<3:
            raise forms.ValidationError("Debe tener al menos 3 letras")

        return direccion


#class RegistroCliente(forms.Form):
 #   nombre=forms.CharField(max_length=25)
  #  rut=forms.CharField(max_length=12)
   # email=forms.EmailField()

class CustomUserForm(UserCreationForm):
   pass

#class PostForm(forms.ModelForm):
#	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

#	class Meta:
#		model = Post
#		fields = ['content']
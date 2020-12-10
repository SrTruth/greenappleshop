from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserForm, RegistroModeloPedido
from datetime import datetime
from .models import Pedido
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as do_logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


# Create your views here. 
def inicio(request):
        return render(request, "inicio.html")


def registro_usuario(request):
    data ={

        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, "te has registrado")
            return redirect('inicio.html')
            

    return render(request,"cuenta.html", data)
    

def login(request):
     # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('inicio.html')

    # Si llegamos al final renderizamos el formulario
    return render(request, "sesion.html", {'form': form})
    

def cerrar(request):
    do_logout(request)

    return redirect('inicio.html')   

@login_required
def pagar(request):
    form=RegistroModeloPedido(request.POST or None)

    if form.is_valid():
        datos=form.cleaned_data
        dire=datos.get("direccion")
        ru=datos.get("rut")
        correo=datos.get("email")
        
        p=Pedido()
        p.direccion=dire
        p.rut=ru
        p.email=correo
        #p.save()
    


    context={
        "formulario":form
    }
    if request.method == 'POST':
        formulari = RegistroModeloPedido(request.POST)
        if formulari.is_valid():
            formulari.save()
            messages.success(request, "Pedido Registrado")
            return redirect('inicio.html')
    
    
    return render(request,"pagar.html",context)
    return redirect('inicio.html')


def tienda(request):
    return render(request,"tienda.html")

def cuenta(request):
    
    return render(request,"cuenta.html")

@login_required
def action(request):

    pedido = Pedido.objects.all()
    data ={'pedidos' : pedido
    }
    

    return render(request, "action_page.html", data)
@login_required
def  modificar_pedido(request,id):

    pedido = get_object_or_404(Pedido, id=id)

    

    dato={
        'form' : RegistroModeloPedido(instance=pedido)

    }
    if request.method =='POST':
        formulario = RegistroModeloPedido(data=request.POST, instance=pedido, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pedido Modificado Exitosamente")
            return redirect('PedidoMod.html')


    return render(request, 'modificar.html',dato)

@login_required
def pedidoMod(request):
    pedido = Pedido.objects.all()
    data ={'pedidos' : pedido
    }
    return render(request,"PedidoMod.html",data)
@login_required
def eliminar_pedido(request,id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect(to="PedidoMod.html")




#def otroform(request):
 #   form=RegistroModeloPersona(request.POST or None)

  #  if form.is_valid():
   #     datos=form.cleaned_data
    #    nom=datos.get("nombre")
     #   correo=datos.get("email")
        
      #  p=Persona()
       # p.nombre=nom
        #p.email=correo
        #p.save()


  #  context={
   #     "formulario":form
    #}
    #return render(request,"otroform.html",context)



#def indec(request):
    #Solo challa
 #   texto="Eso pasa a través de context"
  #  hora=datetime.now()
    #fin challa

   # form=RegistroPersona(request.POST or None)
    #if form.is_valid():
     #   datos=form.cleaned_data
      #  nom=datos.get("nombre")
       # correo=datos.get("email")

        #p=Persona()
        #p.nombre=nom
        #p.email=correo
        #p.save()
    

    #context={
     #   "formulario":form,
      #  "texto":texto,
       # "lahora":hora
    #}
    #return render(request,"indec.html",context)
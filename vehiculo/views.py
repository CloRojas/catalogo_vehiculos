from tokenize import PseudoExtras
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import RegistroUsuarioForm, VehiculoForm
from .models import Vehiculo
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



class IndexPageView(TemplateView):
    template_name = "index.html"

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def lista_vehiculos(request):
    print("Entrando en la vista lista_vehiculos")
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos},  )


@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def vehiculo_view(request):
    context = {}

    form = VehiculoForm(request.POST )
    print("Entrando en la vista vehiculo_vista")

    if form.is_valid():
        print("Formulario válido, guardando datos")
        form.save()
        print("Datos guardados en la base de datos")
        return HttpResponseRedirect('/vehiculo/list') 

    context['form'] = form
    return render(request, 'vehiculo.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Usuario o contraseña inválidos.")
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={"login_form": form})


def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo',
            content_type=content_type)
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro_usuario.html', {'RegistroUsuarioForm': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

from django.shortcuts import render






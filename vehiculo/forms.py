from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
   

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
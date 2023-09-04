
from django.urls import path
from .views import IndexPageView, vehiculo_view, lista_vehiculos, registro_view, login_view, logout_view

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path('vehiculo/add', vehiculo_view, name='vehiculo_view'),
    path('vehiculo/list', lista_vehiculos, name='lista_vehiculos'),
    path('registro/', registro_view, name='registro_usuario'),
    path('login/', login_view, name="login_view"),
     path('logout/', logout_view, name="logout_view"),
]
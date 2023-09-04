from django.apps import AppConfig


class VehiculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehiculo'

    def ready(self):
        from . import models 

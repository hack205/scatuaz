from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar', views.cerrar_sesion, name='cerrar_sesion'),
]

from django.urls import path
from AppCoder import views

urlpatterns = [
    path('padre', views.padre, name=""),
    path('inicio', views.inicio, name="Inicio"),

    path('autoformulario', views.auto_formulario, name = "Auto_formulario"),
    path('inmuebleformulario', views.inmueble_formulario, name = "Inmueble_formulario"),
    path('facultadformulario', views.facultad_formulario, name = "Facultad_formulario"),

    path('autos', views.autos, name="Autos"),
    path('inmuebles', views.inmuebles, name="Inmuebles"),
    path('facultad', views.facultad, name="Facultad"),
]
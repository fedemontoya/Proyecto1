from django.urls import path
from AppCoder import views

urlpatterns = [
    path('padre', views.padre, name=""),
    path('inicio', views.padre, name ="Inicio"),
    path('autosformulario', views.auto_formulario, name = "auto_formulario"),
    #path('inmueblesformulario', views.inmuebles_formulario, name = "inmuebles_formulario"),
    path('autos', views.autos, name="Autos"),
    path('inmuebles', views.inmuebles, name="Inmuebles"),
    path('facultad', views.facultad, name="Facultad"),
]
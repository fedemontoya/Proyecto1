from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from AppCoder.models import Autos, Inmuebles, Facultad
from AppCoder.forms import autoformulario, inmuebleformulario, facultadformulario

# Create your views here.
def padre(request):
    dicc = {"fecha": datetime.today,
    }

    plantilla = loader.get_template("AppCoder/padre.html")

    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def auto_formulario(request):

    if request.method == 'POST':

        mi_formulario = autoformulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            auto_insta = Autos(
            marca = informacion['marca'],
            modelo = informacion['modelo'],
            tipo = informacion['tipo'],
            entregado = informacion['entregado']
            )

            auto_insta.save()

            return render(request, 'AppCoder/inicio.html')

    else:
        mi_formulario = autoformulario()

    return render(request, "AppCoder/autoformulario.html", {"mi_formulario":mi_formulario})

def inmueble_formulario(request):

    if request.method == "POST":
        mi_formulario = inmuebleformulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            inmueble_insta = Inmuebles(
            direccion= informacion['direccion'],
            ciudad= informacion['ciudad'],
             anio= informacion['anio'],
             )

            inmueble_insta.save()

        return render(request, 'AppCoder/inicio.html')

    else:
        mi_formulario = inmuebleformulario()

    return render(request, "AppCoder/inmuebleformulario.html", {"mi_formulario":mi_formulario})

def facultad_formulario(request):

    if request.method == "POST":
        mi_formulario = facultadformulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            facultad_insta = Facultad(
            anio= informacion['anio'],
            carrera= informacion['carrera'],
            universidad= informacion['universidad'],
            email= informacion['email'])

            facultad_insta.save()

        return render(request, 'AppCoder/inicio.html')

    else:
        mi_formulario = facultadformulario()

    return render(request, "AppCoder/facultadformulario.html", {"mi_formulario":mi_formulario})

def autos(request):

    return render(request, 'AppCoder/autos.html')

def inmuebles(request):

    return render(request, 'AppCoder/inmuebles.html')

def facultad(request):

    return render(request, 'AppCoder/facultad.html')


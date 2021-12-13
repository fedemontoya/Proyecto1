from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from AppCoder.models import autos

# Create your views here.
def padre(request):
    dicc = {"fecha": datetime.today,
    "nombre" : "fede"
    }

    plantilla = loader.get_template("AppCoder/inicio.html")

    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def auto_formulario(request):

    if request.method == "POST":
        auto_insta = autos( request.POST['marca'], request.POST['modelo'], request.POST['tipo'], request.POST['entregado'])

        auto_insta.save()

        return render(request, 'AppCoder/inicio.html')

    return render(request, "AppCoder/autoformulario.html")

def facultad_formulario(request):

    if request.method == "POST":
        facultad_insta = facultad( request.POST['anio'], request.POST['carrera'], request.POST['universidad'], request.POST['email'])

        facultad_insta.save()

        return render(request, 'AppCoder/inicio.html')

    return render(request, "AppCoder/facultadformulario.html")

#def inmuebles_formulario(request):

    #if request.method == "POST":
        #inmuebles_insta = inmuebles( request.POST['anio'], request.POST['carrera'], request.POST['universidad'], request.POST['email'])

        #inmuebles_insta.save()

        #return render(request, 'AppCoder/inicio.html')

    #return render(request, "AppCoder/autoformulario.html")

def autos(request):

    return render(request, 'AppCoder/autos.html')

def inmuebles(request):

    return render(request, 'AppCoder/inmuebles.html')

def facultad(request):

    return render(request, 'AppCoder/facultad.html')


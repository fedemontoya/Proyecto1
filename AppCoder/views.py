from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime

# Create your views here.
def inicio(request):
    dicc = {
    "fecha" : datetime.today
    }

    plantilla = loader.get_template("AppCoder/inicio.html")

    documento = plantilla.render(dicc)
    return HttpResponse(documento)
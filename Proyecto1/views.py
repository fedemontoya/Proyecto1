from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def vista(request):
    dicc = {"nombre" : "Fede Montoya",
    "fecha" : datetime.today
    }

    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(dicc)
    return HttpResponse(documento)


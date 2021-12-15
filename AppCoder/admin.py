from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Autos)
admin.site.register(Inmuebles)
admin.site.register(Facultad)
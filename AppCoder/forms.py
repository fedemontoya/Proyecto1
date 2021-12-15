from django import forms

class autoformulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.IntegerField()
    tipo = forms.CharField()
    entregado = forms.BooleanField()

class inmuebleformulario(forms.Form):
    direccion = forms.CharField()
    ciudad = forms.CharField()
    anio = forms.IntegerField()

class facultadformulario(forms.Form):
    anio = forms.IntegerField()
    carrera = forms.CharField()
    universidad = forms.CharField()
    email = forms.EmailField()
from logging import PlaceHolder
from django import forms

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    correo = forms.EmailField()
    salario = forms.IntegerField()

class CursoFormulario(forms.Form):   
    curso = forms.CharField(max_length=30)
    dia = forms.CharField(max_length=40)
    hora = forms.CharField(max_length=40)
    costo = forms.IntegerField()

class AlumnoFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    correo = forms.EmailField()
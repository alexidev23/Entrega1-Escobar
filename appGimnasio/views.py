from errno import ESTALE
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from appGimnasio.models import *
from appGimnasio.forms import *
from django.db.models import Q

# Create your views here.
def inicio(request):
    return render(request, "appGimnasio/index.html")

# Estas son las views para visualizar la BD en la pagina

def cursos(request):
    cursos = Cursos.objects.all() #trae todos los profesores

    contexto= {"cursos":cursos} 

    return render(request, "appGimnasio/cursos.html",contexto)

def alumnos(request):
    alumnos = Alumnos.objects.all() #trae todos los alumnos

    contexto= {"alumnos":alumnos} 

    return render(request, "appGimnasio/alumnos.html",contexto)

def profesores(request):
    profesores = Profesores.objects.all() #trae todos los profesores

    contexto= {"profesores":profesores} 

    return render(request, "appGimnasio/profesores.html",contexto)


#Estas son las views de los formularios para la BD

def formularioCurso(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            curso = Cursos (curso=informacion['curso'], dia=informacion['dia'],
            hora=informacion['hora'],costo=informacion['costo']) 

            curso.save()

            return render(request, "appGimnasio/index.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= CursoFormulario() #Formulario vacio para construir el html

    return render(request, "appGimnasio/formcurso.html", {"miFormulario":miFormulario})

def formularioAlumnos(request):
    if request.method == 'POST':

        miFormulario = AlumnoFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            alumnos = Alumnos (nombre=informacion['nombre'],
            apellido=informacion['apellido'],
            edad=informacion['edad'],
            correo=informacion['correo']) 

            alumnos.save()

            return render(request, "appGimnasio/index.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= AlumnoFormulario() #Formulario vacio para construir el html

    return render(request, "appGimnasio/formalumnos.html", {"miFormulario":miFormulario})

def formularioProf(request):
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            profesor = Profesores (nombre=informacion['nombre'],
            apellido=informacion['apellido'],
            edad=informacion['edad'],
            correo=informacion['correo'],
            salario=informacion['salario']) 

            profesor.save()

            return render(request, "appGimnasio/index.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

    return render(request, "appGimnasio/formProfesor.html", {"miFormulario":miFormulario})

#Estas son las views para buscar


def buscar(request):

    if  request.GET["dia"]: #if request.method == 'Get':

        dia = request.GET['dia'] 
        print(dia)
        cursos = Cursos.objects.filter(dia__icontains=dia)
        print(cursos)
        return render(request, "appGimnasio/cursos.html", {"cursos":cursos,"dia":dia})

    else: 
        respuesta = "No enviaste datos"

    return render(request,"appGimnasio/cursos.html", {"respuesta":respuesta})

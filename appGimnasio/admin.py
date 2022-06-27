from django.contrib import admin

# Register your models here.
from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Profesores)

admin.site.register(Cursos)

admin.site.register(Alumnos)
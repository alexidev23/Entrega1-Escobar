from django.urls import  path
from appGimnasio import views

urlpatterns = [   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('posteos', views.profesores, name="Profesores"),
    path('juegos', views.cursos, name="Cursos"),
    path('perfil', views.alumnos, name="Alumnos"),
    path('profesorform',views.formularioProf,name=
    'Formulario'),
    path('cursoform',views.formularioCurso,name=
    'FormularioCurso'),
    path('alumnoform',views.formularioAlumnos,name=
    'FormularioAlumno'),
    path('buscar/', views.buscar),
]
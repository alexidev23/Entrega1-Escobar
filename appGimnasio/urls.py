from django.urls import  path
from appGimnasio import views

urlpatterns = [   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('profesores', views.profesores, name="Profesores"),
    path('cursos', views.cursos, name="Cursos"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('formulario-profesores',views.formularioProf,name=
    'Formulario'),
    path('formuulario-cursos',views.formularioCurso,name=
    'FormularioCurso'),
    path('formularios-alumnos',views.formularioAlumnos,name=
    'FormularioAlumno'),
    path('buscar/', views.buscar),
]
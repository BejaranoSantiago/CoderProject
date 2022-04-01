from django.urls import path
from .views import curso, entregables, estudiantes, profesores, inicio, cursoFormulario, busquedaCamada, buscar

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('agrega.curso/<nombre>/<camada>/', curso, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('cursoFormulario/', cursoFormulario, name='CursoFormulario'),
    path('busquedaCamada/', busquedaCamada, name='BusquedaCamada'),
    path('buscar/', buscar, name='Buscar'),
]
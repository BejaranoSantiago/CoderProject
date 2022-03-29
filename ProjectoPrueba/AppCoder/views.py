from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def curso(request, nombre, camada):
    mi_curso = Curso(nombre=nombre, camada=camada)
    mi_curso.save()

    return render(request, 'AppCoder/cursos.html', {'nombre':nombre,'camada':camada})

    return HttpResponse(f'Se genero el curso de {mi_curso.nombre} con la camada {mi_curso.camada}')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def inicio(request):
    return HttpResponse(f'Vista de inicio')

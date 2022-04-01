from django.shortcuts import render
from django.http import HttpResponse

from .forms import CursoFormulario
from .models import Curso


# Create your views here.
def curso(request, nombre, camada):
    mi_curso = Curso(nombre=nombre, camada=camada)
    mi_curso.save()

    return render(request, 'AppCoder/cursos.html', {'nombre':nombre,'camada':camada})
    
def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursoFormulario(request):

    if request.method == 'POST':

        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid: #Si paso la validacion de Django

            informacion = mi_formulario.cleaned_data

            nombre= informacion["nombre"]
            camada= informacion["camada"]

            mi_curso = Curso(nombre=nombre, camada=camada)
            mi_curso.save()

            return render(request, 'AppCoder/cursos.html', {'nombre':nombre,'camada':camada})

    else:

        mi_formulario = CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html', {'miForm': mi_formulario})

def busquedaCamada(request):

    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):

    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada = camada)

        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        return HttpResponse("No enviaste el valor de la camada")
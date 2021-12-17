from django.shortcuts import render
from django.http import HttpResponse

from App_1.models import Internos, jefes_de_trabajo,maestros, preceptores
from App_1.forms import formulario_internos

# Create your views here.


def ver_template_index(request):
    return render(request, 'App_1/index.html', {}) 

def ver_template_internos(request):
    if request.method == 'POST':

        miFormulario = formulario_internos(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            internos = Internos(nombre=informacion['nombre'], apellido=informacion['apellido'], trabajo=informacion['trabajo'], 
            horas_de_trabajo=informacion['horas_de_trabajo']) 

            internos.save()

            return render(request, "App_1/index.html")

    else:
        
        miFormulario= formulario_internos() #Formulario vacio para construir el html
            
    return render(request, 'App_1/internos.html', {"miFormulario":miFormulario}) 


def ver_template_jefes(request):
    return render(request, 'App_1/jefes.html', {}) 

def ver_template_maestros(request):
    return render(request, 'App_1/maestros.html', {}) 

def ver_template_preceptores(request):
    return render(request, 'App_1/preceptores.html', {})  
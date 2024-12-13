from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Celular
import random
from inicio.forms import CrearCelular, BuscarCelular


def inicio(resquest):
    return render(resquest, "inicio/inicio.html")
def bienvenida(request):
    return render(request, "inicio/bienvenida.html")
    
def crear_celular (request):
    print(request)
    print(request.GET)
    print(request.POST)
    
    formulario = CrearCelular()
    
    if request.method == "POST":
        formulario = CrearCelular(request.POST)
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            celular = Celular(marca=data.get("marca"),modelo=data.get("modelo"),anio=data.get("anio"))
            celular.save()
            
            return render(request,"inicio/inicio.html")
    
    return render(request, "inicio/crear_celular.html",{"formulario": formulario})

def listado_celulares(request):
    
    formulario_busqueda = BuscarCelular(request.GET)
    
    if formulario_busqueda.is_valid():
        marca_a_buscar = formulario_busqueda.cleaned_data.get("marca")
        modelo_a_buscar = formulario_busqueda.cleaned_data.get("modelo")
        resultado_celulares = Celular.objects.filter(marca__icontains=marca_a_buscar, modelo__icontains=modelo_a_buscar)
    else:
        resultado_celulares = []
    
    return render(request, "inicio/listado_celulares.html",{"listado_celulares": resultado_celulares, "formulario": formulario_busqueda})

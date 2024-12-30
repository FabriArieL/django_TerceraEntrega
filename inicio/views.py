from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Celular
import random
from inicio.forms import CrearCelular, BuscarCelular, EditaCelular
from django.contrib.auth.decorators import login_required


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
            
            return redirect("inicio:listado_celulares")
    
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

def ver_celular(request, id_celular):
    celular = Celular.objects.get(id=id_celular)
    return render(request, "inicio/ver_celular.html", {"celular": celular})

@login_required
def eliminar_celular(request, id_celular):
    celular = Celular.objects.get(id=id_celular)
    
    celular.delete()
    return render(request, "inicio/eliminar_celular.html", {"celular": celular})

@login_required
def editar_celular(request, id_celular):
    celular = Celular.objects.get(id=id_celular)
    
    formulario = EditaCelular(initial={"marca": celular.marca, "modelo": celular.modelo, "anio": celular.anio})
    
    if request.method == "POST":
        formulario = EditaCelular(request.POST)
        if formulario.is_valid():     
            
            celular.marca = formulario.cleaned_data.get("marca")
            celular.modelo = formulario.cleaned_data.get("modelo")
            celular.anio = formulario.cleaned_data.get("anio")
            
            celular.save()
            return redirect("inicio:listado_celulares")
    return render(request, "inicio/editar_celular.html", {"formulario": formulario, "celular": celular})
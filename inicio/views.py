from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Celular
import random


def inicio(resquest):
    return render(resquest, "inicio/inicio.html")
def bienvenida(request):
    return render(request, "inicio/bienvenida.html")

def mi_template(request):
    
    # archivo_abierto = open("templates\mi_template.html")
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    # contexto = Context({"nombre": "Pepe"})
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado) 

    return render(request, "inicio/mi_template.html",{"nombre": "Pepe"})

def mi_template2(request):
    
    # template = loader.get_template("mi_template2.html")
    
    # diccionario = {"nombre": "Pepe"}
    
    # template_renderizado = template.render(diccionario)
    
    # return HttpResponse(template_renderizado) 
    return render(request, "inicio/mi_template2.html")

def condicional_y_bucles(request):
    
    return render(request, 'inicio/condicionales_y_bucles.html', {
        'nombre': 'Ricardo',
        'mis_elementos': [],
        'numero': 2,
        'numeros': list(range(15))
    })
    
def crear_celular(request, marca, modelo, anio):
    # celular = Celular(marca = random.choice(["Motorola","Samsung", "Xiaomi", "Iphone", "Huawei"]), modelo = "Generico", anio = random.choice([2018,2019,2020,2021,2022]))
    celular = Celular(marca = marca, modelo = modelo, anio = anio)
    celular.save()
    return render(request, "inicio/celular_creacion_correcta.html",{"celular": celular})
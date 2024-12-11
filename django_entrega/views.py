from django.http import HttpResponse
from django.template import Template, Context

def bienvenida(request):
    return HttpResponse("<h1>Bienvenida!</h1>")

def mi_template(request):
    
    archivo_abierto = open("templates\mi_template.html")
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    contexto = Context({"nombre": "Pepe"})
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado) 

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from productos.models import Moto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Motos(ListView):
    model = Moto
    template_name = "productos/listado_motos.html"
    context_object_name = "listado_motos"

class CrearMoto(CreateView):
    model = Moto
    template_name = "productos/crear_moto.html"
    fields = ["marca", "anio", "modelo", "imagen"]
    success_url = reverse_lazy("productos:listado_motos")

class VerMoto(DetailView):
    model = Moto
    template_name = "productos/ver_moto.html"
    
class EditarMoto(LoginRequiredMixin,UpdateView):
    model = Moto
    template_name = "productos/editar_moto.html"
    fields = ["marca", "anio", "modelo", "imagen"]
    success_url = reverse_lazy("productos:listado_motos")
    
class EliminarMoto(LoginRequiredMixin,DeleteView):
    model = Moto
    template_name = "productos/eliminar_moto.html"
    success_url = reverse_lazy("productos:listado_motos")



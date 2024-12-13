from inicio.views import crear_celular, inicio, listado_celulares
from django.urls import path, include

app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("celulares/", listado_celulares, name="listado_celulares"),
    path("celulares/crear/", crear_celular, name="crear_celular")
]
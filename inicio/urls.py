from inicio.views import crear_celular, inicio, listado_celulares, ver_celular, eliminar_celular, editar_celular
from django.urls import path, include

app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("celulares/", listado_celulares, name="listado_celulares"),
    path("celulares/crear/", crear_celular, name="crear_celular"),
    path("celulares/<int:id_celular>/", ver_celular, name="ver_celular"),
    path("celulares/<int:id_celular>/eliminar/", eliminar_celular, name="eliminar_celular"),
    path("celulares/<int:id_celular>/editar/", editar_celular, name="editar_celular")

]
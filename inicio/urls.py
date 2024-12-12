from inicio.views import bienvenida, mi_template, mi_template2, condicional_y_bucles, crear_celular, inicio
from django.urls import path, include

app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("bienvenida", bienvenida, name="bienvenida"),
    path("mi-template/", mi_template, name="mi_template"),
    path("mi-template2/", mi_template2, name="mi_template2"),
    path("condicionales-y-bucles/", condicional_y_bucles, name="condicional_y_bucles"),
    path("crear-celular/<str:marca>/<str:modelo>/<int:anio>", crear_celular, name="crear_celular")
]
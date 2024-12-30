from django.urls import path
from productos import views

app_name = "productos"

urlpatterns = [
    path("motos/", views.Motos.as_view(),name="listado_motos"),
    path("motos/crear/", views.CrearMoto.as_view(),name="crear_moto"),
    path("motos/<int:pk>/", views.VerMoto.as_view(),name="ver_moto"),
    path("motos/<int:pk>/editar/", views.EditarMoto.as_view(),name="editar_moto"),
    path("motos/<int:pk>/eliminar/", views.EliminarMoto.as_view(),name="eliminar_moto"),

]

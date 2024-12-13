from django import forms

class CrearCelular(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()

class BuscarCelular(forms.Form):
    marca = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"placeholder":"Motorola, Samsung, Iphone..."}))
    modelo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"placeholder":"Modelo"}))
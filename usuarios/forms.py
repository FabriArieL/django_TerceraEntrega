from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegistroDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label= "Nombre", required=False)
    last_name = forms.CharField(label= "Apellido", required=False)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {
            key: ""
            for key in fields
        }

class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label= "Nombre", required=False)
    last_name = forms.CharField(label= "Apellido", required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name","avatar"]
        
class NuestroCambiarContrasenia(PasswordChangeForm):
    old_password = forms.CharField(label="Vieja Contraseña", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Repetir Nueva Contraseña", widget=forms.PasswordInput)
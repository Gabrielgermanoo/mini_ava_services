from django import forms
from autenticacao.models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'groups']

# forms.py do app "notas"
from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['aluno', 'aula', 'valor']  # O campo professor será preenchido automaticamente

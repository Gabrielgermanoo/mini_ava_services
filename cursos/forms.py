from django import forms
from .models import Curso, Matricula

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao']  # Incluí apenas os campos editáveis
        labels = {
            'nome': 'Nome do Curso',
            'descricao': 'Descrição',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do curso'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição do curso'}),
        }

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso']  # Campos editáveis para Matricula
        labels = {
            'aluno': 'Aluno',
            'curso': 'Curso',
        }
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }

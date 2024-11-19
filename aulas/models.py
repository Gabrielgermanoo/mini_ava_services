from django.db import models
from cursos.models import Curso  # Importando o modelo de Curso para vincular a Aula ao curso
from autenticacao.models import Usuario  # Importando o modelo de Usuario para vincular a Aula ao professor

class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="aulas")
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="aulas")

    def __str__(self):
        return self.titulo

class Material(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="materiais")
    tipo = models.CharField(max_length=10, choices=(("link", "Link"), ("arquivo", "Arquivo")))
    descricao = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)  # Opcional para tipo link
    arquivo = models.FileField(upload_to="materiais/", blank=True, null=True)  # Opcional para tipo arquivo

    def __str__(self):
        return f"{self.descricao} ({self.tipo})"

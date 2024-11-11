from django.db import models
from django.contrib.auth import get_user_model

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
User = get_user_model()

class Matricula(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matriculas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="matriculas")
    data_matricula = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('aluno', 'curso')  # Cada aluno pode estar matriculado uma vez em cada curso

    def __str__(self):
        return f"{self.aluno.username} matriculado em {self.curso.nome}"
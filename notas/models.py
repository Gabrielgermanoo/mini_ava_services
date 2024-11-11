from django.db import models
from django.contrib.auth import get_user_model
from aulas.models import Aula

User = get_user_model()  # Pega o modelo de usuário do projeto (a partir do app de autenticação)

class Nota(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notas")
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="notas")
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('aluno', 'aula')  # Um aluno só pode ter uma nota por aula

    def __str__(self):
        return f"{self.aluno.username} - {self.aula.titulo} - Nota: {self.valor}"

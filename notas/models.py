from django.db import models
from django.contrib.auth import get_user_model
from autenticacao.models import Usuario
from aulas.models import Aula

User = get_user_model()

class Nota(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notas")
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="notas")
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='notas_professor')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('aluno', 'aula')  # Um aluno só pode ter uma nota por aula

    def __str__(self):
        return f"{self.aluno.username} - {self.aula.titulo} - Nota: {self.valor}"

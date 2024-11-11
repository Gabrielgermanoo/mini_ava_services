from rest_framework import serializers
from .models import Nota

class NotaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='aluno.username', read_only=True)
    aula_titulo = serializers.CharField(source='aula.titulo', read_only=True)

    class Meta:
        model = Nota
        fields = ['id', 'aluno', 'aluno_nome', 'aula', 'aula_titulo', 'valor', 'comentarios']
        read_only_fields = ['aluno_nome', 'aula_titulo']  # Campos de exibição

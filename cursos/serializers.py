from rest_framework import serializers
from .models import Curso, Matricula

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao', 'data_criacao']

class MatriculaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='aluno.username', read_only=True)
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)

    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'aluno_nome', 'curso', 'curso_nome', 'data_matricula']
        read_only_fields = ['aluno_nome', 'curso_nome']

from rest_framework import serializers
from .models import Aula, Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'tipo', 'descricao', 'link', 'arquivo']

class AulaSerializer(serializers.ModelSerializer):
    materiais = MaterialSerializer(many=True, read_only=True)  # Permite listar os materiais na mesma resposta

    class Meta:
        model = Aula
        fields = ['id', 'titulo', 'descricao', 'data', 'curso', 'materiais']

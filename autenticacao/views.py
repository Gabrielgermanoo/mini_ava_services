from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import UsuarioSerializer
from autenticacao.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint para listar, criar, editar e excluir usuários.
    Somente administradores têm permissão para acessar.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]
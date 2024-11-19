from django.urls import path
from autenticacao.views import listar_usuarios, adicionar_usuario, editar_usuario, excluir_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/editar/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:pk>/', excluir_usuario, name='excluir_usuario'),
]

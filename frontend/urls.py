# frontend/urls.py

from django.urls import path
from . import views
from .views import listar_usuarios, adicionar_usuario, editar_usuario, excluir_usuario
from .views import listar_notas, adicionar_nota, editar_nota, excluir_nota
from .views import listar_cursos, adicionar_curso, editar_curso, excluir_curso
from .views import listar_aulas, adicionar_aula, editar_aula, excluir_aula

urlpatterns = [
    path('', views.index, name='index'),
    path('aulas/', listar_aulas, name='listar_aulas'),
    path('aulas/listar', listar_aulas, name='listar_aula'),
    path('aulas/adicionar/', adicionar_aula, name='adicionar_aula'),
    path('aulas/editar/<int:pk>/', editar_aula, name='editar_aula'),
    path('aulas/excluir/<int:pk>/', excluir_aula, name='excluir_aula'),
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('cursos/listar', listar_cursos, name='listar_curso'),
    path('cursos/adicionar/', adicionar_curso, name='adicionar_curso'),
    path('cursos/editar/<int:pk>/', editar_curso, name='editar_curso'),
    path('cursos/excluir/<int:pk>/', excluir_curso, name='excluir_curso'),
    path('notas/', views.notas, name='notas'),
    path('notas/listar',listar_notas, name='listar_notas'),
    path('notas/adicionar/', adicionar_nota, name='adicionar_nota'),
    path('notas/editar/<int:pk>/', editar_nota, name='editar_nota'),
    path('notas/excluir/<int:pk>/', excluir_nota, name='excluir_nota'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/editar/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:pk>/', excluir_usuario, name='excluir_usuario'),
    path('login/', views.LoginPageView.as_view(next_page='/'), name='login'),  # Rota para login
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
]

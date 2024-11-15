# frontend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aulas/', views.aulas, name='aulas'),
    path('cursos/', views.cursos, name='cursos'),
    path('notas/', views.notas, name='notas'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('login/', views.LoginPageView.as_view(), name='login'),  # Rota para login
    path('logout/', views.LogoutPageView.as_view(), name='logout'),  # Rota para logout
]

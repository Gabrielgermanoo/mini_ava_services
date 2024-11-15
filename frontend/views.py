# frontend/views.py

from django.shortcuts import render
from aulas.models import Aula
from cursos.models import Curso
from notas.models import Nota
from autenticacao.models import Usuario
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def index(request):
    return render(request, 'frontend/index.html')

@login_required
def aulas(request):
    lista_aulas = Aula.objects.all()
    return render(request, 'frontend/aulas.html')

@login_required
def cursos(request):
    lista_cursos = Curso.objects.all()
    return render(request, 'frontend/cursos.html', {'cursos': lista_cursos})

@login_required
def notas(request):
    lista_notas = Nota.objects.select_related('aluno', 'aula__curso') 
    return render(request, 'frontend/notas.html', {'notas': lista_notas})

@login_required
def usuarios(request):
    lista_usuarios = Usuario.objects.all()  # Obtenha todos os usuários do banco de dados
    return render(request, 'frontend/usuarios.html', {'usuarios': lista_usuarios})


class LoginPageView(LoginView):
    template_name = 'frontend/login.html'

class LogoutPageView(LogoutView):
    pass
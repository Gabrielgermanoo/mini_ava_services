from django.shortcuts import render, get_object_or_404
from aulas.models import Aula
from cursos.models import Curso
from notas.models import Nota
from autenticacao.models import Usuario
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.db.models import Q
from notas.forms import NotaForm 
from cursos.forms import CursoForm
from aulas.forms import AulaForm


@login_required
def listar_usuarios(request):
    """
    Lista todos os usuários cadastrados.
    """
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

@login_required
def adicionar_usuario(request):
    """
    Adiciona um novo usuário.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            # Adiciona o usuário a um grupo, se necessário
            grupo = request.POST.get('grupo')
            if grupo:
                grupo_obj = Group.objects.get(name=grupo)
                usuario.groups.add(grupo_obj)
            return redirect('listar_usuarios')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/form.html', {'form': form, 'titulo': 'Adicionar Usuário'})

from django.contrib.auth.forms import UserChangeForm

@login_required
def editar_usuario(request, pk):
    """
    Edita um usuário existente.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UserChangeForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form, 'titulo': 'Editar Usuário'})

@login_required
def excluir_usuario(request, pk):
    """
    Exclui um usuário.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/excluir.html', {'usuario': usuario})

@login_required
def listar_notas(request):
    """Lista todas as notas de acordo com o tipo de usuário."""
    usuario = request.user
    if usuario.is_superuser:  # Administrador
        notas = Nota.objects.all()
    elif usuario.groups.filter(name='Professor').exists():  # Professor
        notas = Nota.objects.filter(professor=usuario)
    else:  # Aluno
        notas = Nota.objects.filter(aluno=usuario)
    return render(request, 'notas/listar.html', {'notas': notas})

@login_required
def adicionar_nota(request):
    """Adiciona uma nova nota."""
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            # Se o usuário for professor, associa automaticamente
            if request.user.groups.filter(name='Professor').exists():
                nota.professor = request.user
            nota.save()
            return redirect('listar_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/form.html', {'form': form, 'titulo': 'Adicionar Nota'})


@login_required
def editar_nota(request, pk):
    """Edita uma nota existente."""
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/form.html', {'form': form, 'titulo': 'Editar Nota'})


@login_required
def excluir_nota(request, pk):
    """Exclui uma nota."""
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('listar_notas')
    return render(request, 'notas/excluir.html', {'nota': nota})

@login_required
def index(request):
    """
    Página inicial do sistema. Requer autenticação.
    """
    return render(request, 'frontend/index.html')

@login_required
def notas(request):
    """
    Filtra e exibe as notas com base no tipo de usuário.
    - Professores: veem notas das aulas que ministram.
    - Alunos: veem suas próprias notas.
    - Administradores: veem todas as notas.
    """
    user = request.user
    if user.groups.filter(name='Professor').exists():
        usuario = Usuario.objects.get(username=user)
        lista_notas = Nota.objects.filter(aula__professor=usuario).select_related('aluno', 'aula__curso')
    elif user.groups.filter(name='Aluno').exists():
        lista_notas = Nota.objects.filter(aluno=user).select_related('aluno', 'aula__curso')
    else:  # Administradores ou usuários sem grupo específico
        lista_notas = Nota.objects.select_related('aluno', 'aula__curso')
    
    return render(request, 'notas/listar.html', {'notas': lista_notas})


@login_required
def usuarios(request):
    """
    Lista todos os usuários cadastrados.
    """
    lista_usuarios = Usuario.objects.all()
    return render(request, 'frontend/usuarios.html', {'usuarios': lista_usuarios})

@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar.html', {'cursos': cursos})

# Adicionar curso
@login_required
def adicionar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/forms.html', {'form': form})

# Editar curso
@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/forms.html', {'form': form, 'curso': curso})

# Excluir curso
@login_required
def excluir_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == "POST":
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'cursos/excluir.html', {'curso': curso})

@login_required
def listar_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/listar.html', {'aulas': aulas})

@login_required
def adicionar_aula(request):
    if request.method == "POST":
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulaForm()
    return render(request, 'aulas/forms.html', {'form': form})

@login_required
def editar_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    if request.method == "POST":
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulaForm(instance=aula)
    return render(request, 'aulas/forms.html', {'form': form, 'aula': aula})

@login_required
def excluir_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    if request.method == "POST":
        aula.delete()
        return redirect('listar_aulas')
    return render(request, 'aulas/excluir.html', {'aula': aula})


class LoginPageView(LoginView):
    """
    Página de login.
    """
    template_name = 'frontend/login.html'


class LogoutPageView(LogoutView):
    """
    Página de logout. Redireciona para o login após sair.
    """
    next_page = '/'

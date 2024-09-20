from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm
from .models import Livro, Emprestimo, Contato  # Certifique-se de que Emprestimo e Contato estão incluídos


def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('acervo_pessoal:listar_livros')  # Corrigido para usar o namespace
    else:
        form = LivroForm()
    return render(request, 'acervo_pessoal/adicionar_livros.html', {'form': form})

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo_pessoal/listar_livros.html', {'livros': livros})

def detalhes_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'acervo_pessoal/detalhes_livro.html', {'livro': livro})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('acervo_pessoal:listar_livros')  # Corrigido para usar o namespace
    else:
        form = LivroForm(instance=livro)
    return render(request, 'acervo_pessoal/editar_livro.html', {'form': form})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('acervo_pessoal:listar_livros')  # Corrigido para usar o namespace
    return render(request, 'acervo_pessoal/deletar_livro.html', {'livro': livro})

# Cadastro de usuário
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Faz o login do usuário após o registro
            return redirect('acervo_pessoal:listar_livros')  # Redireciona para a lista de livros
    else:
        form = UserCreationForm()
    return render(request, 'acervo_pessoal/registro_usuario.html', {'form': form})

# Login de usuário
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('acervo_pessoal:listar_livros')  # Redireciona para a lista de livros
    else:
        form = AuthenticationForm()
    return render(request, 'acervo_pessoal/login_usuario.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('acervo_pessoal:listar_livros')  # Redireciona para a lista de livros

@login_required
def perfil(request):
    user = request.user
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('acervo_pessoal:perfil')  # Verifique se o namespace e o nome da URL estão corretos
    else:
        form = PerfilForm(instance=user)
    return render(request, 'acervo_pessoal/perfil.html', {'form': form, 'user': user})

def emprestimo(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        contato_id = request.POST.get('contato_id')  # Verifique se o contato está sendo passado corretamente
        data_emprestimo = request.POST.get('data_emprestimo')

        # Verifique se contato_id e data_emprestimo não estão vazios
        if contato_id and data_emprestimo:
            emprestimo = Emprestimo(livro=livro, contato_id=contato_id, data_emprestimo=data_emprestimo)
            emprestimo.save()
            return redirect('acervo_pessoal:listar_livros')
    else:
        contatos = Contato.objects.all()  # Busque todos os contatos
    return render(request, 'acervo_pessoal/emprestimo.html', {'livro': livro, 'contatos': contatos})


from django.urls import path
from . import views

app_name = 'acervo_pessoal'

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('livros/<int:id>/', views.detalhes_livro, name='detalhes_livro'),
    path('livros/<int:id>/editar/', views.editar_livro, name='editar_livro'),
    path('livros/<int:id>/deletar/', views.deletar_livro, name='deletar_livro'),
    path('livros/<int:id>/emprestimo/', views.emprestimo, name='emprestimo'),  # Verifique esta linha
    path('register/', views.register, name='registro_usuario'),
    path('login/', views.login, name='login_usuario'),
    path('logout/', views.logout, name='logout_usuario'),
    path('perfil/', views.perfil, name='perfil'),
]

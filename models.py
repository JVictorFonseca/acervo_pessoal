from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    foto_capa = models.ImageField(upload_to='capas/')

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    # Você pode adicionar mais campos, como data_devolucao, se necessário

    def __str__(self):
        return f'{self.livro.titulo} emprestado para {self.contato.nome} por {self.usuario.username}'
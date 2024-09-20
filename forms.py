from django import forms
from .models import Livro
from django.contrib.auth.models import User

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao', 'foto_capa']  # Ajuste os campos conforme necessário


class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos do perfil a serem editados

class EmprestimoForm(forms.Form):
    CONTATO_CHOICES = [
        ('celular', 'Celular'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
    ]

    tipo_contato = forms.ChoiceField(choices=CONTATO_CHOICES, label='Tipo de Contato')
    contato = forms.CharField(max_length=100, label='Contato', widget=forms.TextInput(attrs={'placeholder': 'Digite o contato'}))
    data_emprestimo = forms.DateField(label='Data do Empréstimo', widget=forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa'}))
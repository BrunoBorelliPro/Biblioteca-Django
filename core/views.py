from dataclasses import fields
from pyexpat import model
from django.views.generic import ListView, CreateView

from core.models import Livro, Emprestimo

class LivrosListView(ListView):
    model = Livro

class LivrosCreateView(CreateView):
    model = Livro
    fields = '__all__'

class EmprestimosListView(ListView):
    model = Emprestimo

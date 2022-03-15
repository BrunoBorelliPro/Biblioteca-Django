from django.views.generic import ListView

from core.models import Livros

class LivrosListView(ListView):
    model = Livros

class EmprestimosListView(ListView):
    model = Livros

class UsuariosListView(ListView):
    model = Livros
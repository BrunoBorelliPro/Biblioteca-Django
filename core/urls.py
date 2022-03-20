from django.urls import path

from .views import LivrosCreateView, LivrosListView

app_name = 'core'

urlpatterns = [
    path('livros', LivrosListView.as_view(), name="livros"),
    path('livros/createlivro', LivrosCreateView.as_view(), name="createlivro"),
    path('emprestimos', LivrosListView.as_view(), name="emprestimos"),
    path('usuarios', LivrosListView.as_view(), name="usuarios"),
]

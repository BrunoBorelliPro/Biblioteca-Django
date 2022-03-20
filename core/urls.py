from django.urls import path

from .views import(
    LivrosListView,
    LivroCreateView,
    LivroDeleteView,
    LivroUpdateView,
    LivroDetailView,

    AutorCreateView,
    AutorListView,
    AutorDeleteView,
    AutorUpdateView,

    ReservasListView,
    UserReservasListView,
    LivrosDisponiveisListView,
    ReservaDeleteView,
    ReservaAdminDeleteView)

app_name = 'core'

urlpatterns = [
    # Reserva urls
    path('livros_disponiveis/', LivrosDisponiveisListView.as_view(), name="livros_disponiveis"),
    path('reservas/', ReservasListView.as_view(), name='visualizar_reservas'),
    path('minhas_reservas/', UserReservasListView.as_view(), name='minhas_reservas'),
    path('<pk>/deletar_reserva/', ReservaDeleteView.as_view(), name='deletar_reserva'),
    path('<pk>/deletar_reserva_admin/', ReservaAdminDeleteView.as_view(), name='deletar_reserva_admin'),

    # Autor urls
    path('create_autor/', AutorCreateView.as_view(), name='create_autor'),
    path('list_autor/', AutorListView.as_view(), name='list_autor'),
    path('<pk>/delete_autor/', AutorDeleteView.as_view(), name='delete_autor'),
    path('<pk>/update_autor/', AutorUpdateView.as_view(), name='update_autor'),

    # Livro urls
    path('list_livro/', LivrosListView.as_view(), name="list_livro"),
    path('create_livro/', LivroCreateView.as_view(), name="create_livro"),
    path('<pk>/delete_livro/', LivroDeleteView.as_view(), name='delete_livro'),
    path('<pk>/update_livro/', LivroUpdateView.as_view(), name='update_livro'),
    path('<pk>/detail_livro/', LivroDetailView.as_view(), name='detail_livro'),


]

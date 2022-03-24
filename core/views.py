from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from core.models import Autor, Livro, Reserva
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator

class LivrosDisponiveisListView(ListView):
    model = Livro
    @method_decorator(login_required)
    def get(self, request):
        """Lista os livros disponiveis para reserva"""
        livro_list = self.livros_disponiveis()
        context = {
            'livro_list': livro_list,
            'user': User.objects.get(username=request.user)
        }
        return render(request, 'core/livro_list.html', context)

    
    @method_decorator(login_required)
    def post(self, request):
        """Reserva o livro"""
        livro_id = request.POST['livro_id']
        livro = Livro.objects.get(id=livro_id)
        user = User.objects.get(username=request.user)
        reserva = Reserva(livro = livro, user=user)
        reserva.save()
        livro_list = self.livros_disponiveis()
        context = {
            'livro_list': livro_list,
            'user': User.objects.get(username=request.user)
        }
        return render(request, 'core/livro_list.html', context)

    def livros_disponiveis(self):
        return Livro.objects.all().exclude(reserva__reservado=True)




class ReservasListView(PermissionRequiredMixin, ListView):
    permission_required = 'is_staff'
    model = Reserva
    template_name = 'painel_admin/reserva_list.html'

class UserReservasListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'core/minhas_reservas.html'
    def get_queryset(self):
        queryset = Reserva.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    success_url = '/biblioteca/minhas_reservas'
    template_name = "core/delete.html"

class ReservaAdminDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'

    model = Reserva
    success_url = '/biblioteca/reservas/'
    template_name = "painel_admin/delete.html"
    

class AutorListView(PermissionRequiredMixin, ListView):
    permission_required = 'is_staff'
    model = Autor
    template_name = "painel_admin/autor/autor_list.html"

class AutorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Autor
    fields = '__all__'
    template_name = "painel_admin/autor/autor_form.html"
    success_url = '/biblioteca/list_autor/'


class AutorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Autor
    template_name = "painel_admin/autor/autor_form.html"
    fields = '__all__'
    success_url = '/biblioteca/list_autor/'
    permission_required = 'is_staff'

class AutorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Autor
    template_name = "painel_admin/delete.html"
    success_url = '/biblioteca/list_autor/'
    permission_required = 'is_staff'



class LivrosListView(ListView):
    model = Livro
    template_name = 'core/livro/todos_os_livros.html'

class LivroCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    template_name = "core/livro/livro_form.html"
    model = Livro
    fields = '__all__'

class LivroUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_staff'
    model = Livro
    template_name = "core/livro/livro_form.html"
    fields = '__all__'

class LivroDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'
    model = Livro
    template_name = "core/delete.html"
    success_url = '/biblioteca/list_livro/'

class LivroDetailView(DetailView):
    model = Livro
    template_name = "core/livro/detail_livro.html"


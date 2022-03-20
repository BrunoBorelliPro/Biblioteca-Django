
from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from users.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

class UsersListView(PermissionRequiredMixin, ListView):
    permission_required = 'users.user.action_all'
    model = User
    context_object_name = "user_view"

class UserCreateView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = "users/cadastro_users.html"
    context_object_name = "user_view"
    success_url = '/'

class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.user.action_all'
    model = User
    template_name = "users/update_users.html"
    fields = ['username', 'first_name', 'last_name', 'email']
    context_object_name = "user_view"
    success_url = '/'


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.user.action_all'
    model = User
    template_name = "users/delete.html"
    success_url = '/'
    context_object_name = "user_view"


class UserDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'users.user.action_all'

    model = User
    template_name = "users/detalhar_user.html"
    context_object_name = "user_view"


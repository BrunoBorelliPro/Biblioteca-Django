import re
from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User

class HomePageView(TemplateView):
    template_name = "home.html"

class AdminView(TemplateView):
    template_name = "painel_admin/home_admin.html"

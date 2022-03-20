import re
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from users.models import User

class HomePageView(TemplateView):
    template_name = "home.html"

class AdminView(PermissionRequiredMixin, TemplateView):
    template_name = "painel_admin/home_admin.html"
    permission_required = 'is_staff'
import re
from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User

def home_page(request):
    if not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
    else:
        user = False
    context = {
        'user': user
    }
    print(request.user)
    return render(request, 'home.html', context)
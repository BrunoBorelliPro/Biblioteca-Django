from django.contrib import admin

from core.models import Livros

@admin.register(Livros)
class AdminLivros(admin.ModelAdmin):
    pass

from django.contrib import admin

from core.models import Livro, Emprestimo, Autor

@admin.register(Livro)
class AdminLivro(admin.ModelAdmin):
    pass

@admin.register(Emprestimo)
class AdminEmprestimo(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
    pass
from django.contrib import admin

from core.models import Livro, Autor, Reserva

@admin.register(Livro)
class AdminLivro(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
    pass

@admin.register(Reserva)
class AdminReserva(admin.ModelAdmin):
    pass
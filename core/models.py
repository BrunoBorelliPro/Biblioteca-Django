from django.db import models
from django.urls import reverse
class Autor(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome
    
class Livro(models.Model):

    titulo = models.CharField(max_length=100)
    sinopse = models.TextField()
    autor = models.ForeignKey("core.Autor", on_delete=models.CASCADE)
    capa = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def get_absolute_url(self):
        return reverse("core:detail_livro", kwargs={"pk": self.pk})

class Reserva(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    livro = models.ForeignKey("core.Livro", on_delete=models.CASCADE)
    reservado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f'{self.user} | {self.livro}'

    def get_absolute_url(self):
        return reverse("core:deletar_reserva", kwargs={"pk": self.pk})
    



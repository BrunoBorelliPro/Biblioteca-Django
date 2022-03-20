from django.db import models

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

class Emprestimo(models.Model):

    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    livro = models.ForeignKey("Livro", on_delete=models.CASCADE)
    ativo = models.BooleanField()
    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"

    def __str__(self):
        return f'{self.livro} - {self.user}'


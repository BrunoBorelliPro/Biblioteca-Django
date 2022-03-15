from distutils.command.upload import upload
from turtle import title
from django.db import models

class Livros(models.Model):

    title = models.CharField(max_length=100)
    sinopse = models.TextField()
    autor = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
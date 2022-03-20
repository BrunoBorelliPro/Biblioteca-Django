from django import forms

from core.models import Livro, Emprestimo

class LivroCreate(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'sinopse', 'autor', 'capa')

        widget = {
            'titulo': forms.CharField(attrs={'class': 'form-control'}),
            'sinopse': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.CharField(attrs={'class': 'form-control'}),
            'capa': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EmprestimoCreate(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
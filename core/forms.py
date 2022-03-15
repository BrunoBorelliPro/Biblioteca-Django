from django.forms import ModelForm

from core.models import Livros

class LivroCreate(ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
# Generated by Django 4.0.3 on 2022-03-15 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livros',
            new_name='Livro',
        ),
        migrations.RenameField(
            model_name='livro',
            old_name='title',
            new_name='titulo',
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.livro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
    ]
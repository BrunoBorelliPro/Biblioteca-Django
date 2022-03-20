# Generated by Django 4.0.3 on 2022-03-16 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_autor_alter_livro_options_alter_livro_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='ativo',
            new_name='devolvido',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
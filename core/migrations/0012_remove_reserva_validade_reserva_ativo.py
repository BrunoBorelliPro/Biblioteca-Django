# Generated by Django 4.0.3 on 2022-03-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_reserva_validade_delete_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='validade',
        ),
        migrations.AddField(
            model_name='reserva',
            name='ativo',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-16 12:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_alter_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_prevista_devolucao',
            field=models.DateField(default=datetime.datetime(2022, 3, 23, 9, 15, 47, 417626)),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validade', models.DateField(default=datetime.datetime(2022, 3, 19, 9, 15, 47, 417626))),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.livro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-17 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_emprestimo_data_prevista_devolucao_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='validade',
            field=models.DateField(default=datetime.datetime(2022, 3, 20, 11, 8, 34, 130141)),
        ),
        migrations.DeleteModel(
            name='Emprestimo',
        ),
    ]

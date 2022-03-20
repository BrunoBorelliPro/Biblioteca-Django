# Generated by Django 4.0.3 on 2022-03-16 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_prevista_devolucao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
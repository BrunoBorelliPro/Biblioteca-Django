# Generated by Django 4.0.3 on 2022-03-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_prevista_devolucao',
            field=models.DateField(),
        ),
    ]
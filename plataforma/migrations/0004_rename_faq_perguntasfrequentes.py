# Generated by Django 4.0.4 on 2022-06-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_remove_duvida_descricao_resposta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQ',
            new_name='PerguntasFrequentes',
        ),
    ]

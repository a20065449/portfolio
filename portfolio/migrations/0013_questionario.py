# Generated by Django 4.0.4 on 2022-06-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_educacao_curso_alter_educacao_qualificacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=200, null=True)),
                ('opcao1', models.CharField(max_length=200, null=True)),
                ('opcao2', models.CharField(max_length=200, null=True)),
                ('opcao3', models.CharField(max_length=200, null=True)),
                ('opcao4', models.CharField(max_length=200, null=True)),
                ('resposta', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

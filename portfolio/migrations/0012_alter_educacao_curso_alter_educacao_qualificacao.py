# Generated by Django 4.0.4 on 2022-06-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_educacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacao',
            name='curso',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='educacao',
            name='qualificacao',
            field=models.CharField(max_length=50),
        ),
    ]

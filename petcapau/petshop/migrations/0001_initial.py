# Generated by Django 3.0.5 on 2022-04-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nome')),
                ('species', models.CharField(max_length=70, verbose_name='Espécie')),
                ('breed', models.CharField(max_length=70, verbose_name='Raça')),
                ('sex', models.CharField(choices=[('Macho', 'Macho'), ('Femea', 'Femea')], default='Macho', max_length=5, verbose_name='Sexo')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('hair', models.CharField(choices=[('Macho', 'Macho'), ('Femea', 'Femea')], default='curto', max_length=12, verbose_name='Sexo')),
                ('tatoo', models.CharField(max_length=7, verbose_name='Identificação ou Tatuagem')),
            ],
        ),
    ]

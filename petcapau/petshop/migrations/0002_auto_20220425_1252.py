# Generated by Django 3.0.5 on 2022-04-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='hair',
            field=models.CharField(choices=[('curto', 'curto'), ('longo', 'longo'), ('encaracolado', 'encaracolado'), ('duplo', 'duplo')], default='curto', max_length=12, verbose_name='Pelagem'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='tatoo',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Identificação ou Tatuagem'),
        ),
    ]
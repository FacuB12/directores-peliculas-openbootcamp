# Generated by Django 4.1.7 on 2023-03-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directores_cine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='director',
            name='nacionalidad',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='director',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(help_text='La descripcion de la pelicula', max_length=1000),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-01 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(help_text='La descripcion de la peli', max_length=1000)),
                ('fecha_estreno', models.DateField()),
                ('duracion_minutos', models.IntegerField()),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directores_cine.director')),
            ],
        ),
    ]

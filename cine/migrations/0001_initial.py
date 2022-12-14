# Generated by Django 4.1.2 on 2022-10-29 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('mumero_asientos', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.cine')),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('hora_inicio', models.DateTimeField()),
                ('hora_fin', models.DateTimeField()),
                ('valor', models.IntegerField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.pelicula')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('asientos', models.CharField(max_length=50)),
                ('valor_boleta', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.cliente')),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.funcion')),
            ],
        ),
    ]

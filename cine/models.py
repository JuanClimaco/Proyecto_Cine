from django.db import models

class Cine(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

class Sala(models.Model):
    cine = models.ForeignKey(Cine,on_delete= models.PROTECT)
    nombre = models.CharField(max_length=20)
    mumero_asientos = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField(max_length= 50)
    telefono = models.CharField(max_length =50)
    correo = models.CharField(max_length =50)

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala,on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now= False)
    hora_inicio = models.DateTimeField(auto_now= False)
    hora_fin= models.DateTimeField(auto_now=False)
    valor = models.IntegerField()

class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now=True)
    asientos = models.CharField(max_length=50)
    valor_boleta = models.IntegerField()





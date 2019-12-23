from django.db import models

class Peluquero(models.Model):
	cedula = models.CharField("Cédula",max_length=9,unique=True)
	nombre = models.CharField("Nombre",max_length=20)
	apellido = models.CharField("Apellido",max_length=20)
	direccion = models.TextField()
	telefono = models.CharField("Teléfono",max_length=11)

	def __init__(self):
		return self.nombre


class Servicios(models.Model):
	nombre = models.CharField('Servicio', max_length=30,unique=True)
	precio = models.FloatField()
	descripcion = models.TextField()
	imagen = models.ImageField(null=True,blank=True)



class ImgCarrucel(models.Model):
	img1 = models.ImageField(null=True,blank=True)
	img2 = models.ImageField(null=True,blank=True)
	img3 = models.ImageField(null=True,blank=True)
	img4 = models.ImageField(null=True,blank=True)


class diseñoGeneral(models.Model):
	titulo = models.CharField('Titulo',max_length=40)

class Galeria(models.Model):
	imagen = models.ImageField()

class Reservacion(models.Model):
	pass


from  __future__  import  unicode_literals 
from django.db import models


# Create your models here.
class Registro(models.Model):
	correo = models.EmailField(max_length=25, blank=True)
	asunto = models.CharField(max_length=25, blank=True)
	mensaje = models.CharField(max_length=120, blank=True)
	adjuntar = models.CharField(max_length=120, blank=True)


	def __unicode__(self):
		return self.correo
		
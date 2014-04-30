from django.db import models

# Create your models here.

class Materiel(models.Model):
		nom = models.CharField(max_length=200)
		ville = models.CharField(max_length=200)
		adresse = models.CharField(max_length=200)
		telephone = models.CharField(max_length=200)
		def __unicode__(self):
				return self.nom
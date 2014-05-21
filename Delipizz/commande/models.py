from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#extension du User
class Customer(models.Model):
    user = models.OneToOneField(User, unique=True,related_name='profile')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)


class Materiel(models.Model):
		nom = models.CharField(max_length=200)
		ville = models.CharField(max_length=200)
		addresse = models.CharField(max_length=200)
		telephone = models.CharField(max_length=200)
		def __unicode__(self):
				return self.nom
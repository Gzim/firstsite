from django.db import models

class Auto(models.Model):
	user = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	marke = models.CharField(max_length=50, blank=True)
	kanton = models.CharField(max_length=50, blank=True)
	preis = models.IntegerField(null=True, blank=True)

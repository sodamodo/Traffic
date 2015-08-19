from django.contrib.gis.db import models

# Create your models here.
class Roads(models.Model):
    street = models.CharField()


    poly = models.MultiLineStringField()
    objects = models.GeoManager()
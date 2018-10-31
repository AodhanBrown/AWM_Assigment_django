#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Maps(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

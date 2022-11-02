from django.db import models

class Familia(models.Model):
    nombre= models.CharField(max_lenght=40)
    apellido= models.CharField(max_leght=40)
    edad= models.IntegerField()
    fecha_nacimiento= models.DateField()
    
    

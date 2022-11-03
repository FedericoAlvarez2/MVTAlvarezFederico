from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context, loader
from appfamilia.models import Familia
 



def familia (self):
  flia1 = Familia(nombre= "Daniel", apellido= "Alvarez", edad= 72, fecha_nacimiento= "1950-02-10")
  flia1.save()
    
  flia2 = Familia(nombre= "Norma", apellido= "Cerduca", edad= 70, fecha_nacimiento= "1952-11-30")
  flia2.save()

  flia3 = Familia(nombre= "Ximena", apellido= "Alvarez", edad= 35, fecha_nacimiento= "1987-12-02")
  flia3.save()

  flia4 = Familia(nombre= "Federico", apellido = "Alvarez", edad= 30, fecha_nacimiento = "1992-03-12")
  flia4.save()

  plantilla = loader.get_template("plantilla.html")
  familia = {"familia": [flia1, flia2, flia3, flia4]}
  documento = plantilla.render(familia)
  return HttpResponse(documento)
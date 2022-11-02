from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from appfamilia.models import Familia




def familia (self):
  flia1 = Familia(nombre= "Daniel", apellido= "Alvarez", edad= 72, fecha_nacimiento= "14-02-1950")
  flia1.save()
    
  flia2 = Familia(nombre= "Norma", apellido= "Cerduca", edad= 70, fecha_nacimiento= "02-12-1952")
  flia2.save()

  flia3 = Familia(nombre= "Ximena", apellido= "Alvarez", edad= 35, fecha_nacimiento= "19-12-1987")
  flia3.save()

  flia4 = Familia(nombre= "Federico", apellido = "Alvarez", edad= 30, fecha_nacimiento = "12-03-1992")
  flia4.save()

  plantilla = loader.get_template("plantilla.html")
  familiares = {"familia": [flia1, flia2, flia3, flia4]}
  documento = plantilla.render(familiares)
  return HttpResponse(documento)
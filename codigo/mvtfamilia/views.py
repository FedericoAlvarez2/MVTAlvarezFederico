from django.http import HttpResponse
from django.template import Template, Context, loader
from mvtfamilia.models import Familia




#def familia (self):
 # flia1 = Familia(nombre= "Daniel", apellido= "Alvarez", edad= 72, dni= 7543234)
 # flia1.save()
    
 # flia2 = Familia(nombre= "Norma", apellido= "Cerduca", edad= 70, dni= 10545254)
 # flia2.save()
#
 # flia3 = Familia(nombre= "Ximena", apellido= "Alvarez", edad= 35, dni= 34324566)
 # flia3.save()

 # flia4 = Familia(nombre= "Federico", apellido = "Alvarez", edad= 30, dni= 36233603)
 # flia4.save()

 # diccionario = "nombre", {flia1.nombre}, "apellido", {flia1.apellido}, "edad", {flia1.edad}, "dni" ,{flia1.dni}, "nombre", {flia2.nombre}, "apellido", {flia2.apellido}, "edad", {flia2.edad}, "dni", {flia2.dni}, "nombre", {flia3.nombre}, "apellido", {flia3.apellido}, "edad", {flia3.edad}, "dni", {flia3.dni}, "nombre", {flia4.nombre}, "apellido",{flia4.apellido}, "edad", {flia4.edad}, "dni", {flia4.dni}

 # return HttpResponse(diccionario)
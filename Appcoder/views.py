
from smtplib import SMTPResponseException
from tkinter.filedialog import Open
from django.shortcuts import render
from django.http import HttpResponse
from .models import Madre
from .models import Sobrino
from .models import Sobrina 
from django.template import Context, Template

def inicio(request):
    return render(request,"Appcoder/inicio.html")

def madre(request):
    madre=Madre(nombre="Maria", dni="12565656", fecha_nacimiento="1963-11-29")
    madre.save()
    texto=f"Madre: nombre: {madre.nombre} dni: {madre.dni} fecha_nacimiento: {madre.fecha_nacimiento}"
    return render(request,"Appcoder/madre.html")
  
    
def sobrino(request):
    sobrino=Sobrino(nombre="Thomas", email=("tho@mas"), fecha_nacimiento="2000-1-12")
    sobrino.save()
    texto=f"Sobrino: nombre: {sobrino.nombre} emial: {sobrino.email} fecha_nacimiento: {sobrino.fecha_nacimiento}"
    return render(request,"Appcoder/sobrino.html")

def sobrina(request):
    sobrina=Sobrina(nombre="Juana",colegio="San Agustin",examenes="7")
    sobrina.save()
    texto=f"Sobrina: nombre: {sobrina.nombre} colegio: {sobrina.colegio} examenes: {sobrina.examenes}"
    return render(request,"Appcoder/sobrina.html")
from django.shortcuts import render,HttpResponse
from servicios.models import Servicios
# Create your views here.

def servicios(request):
    servicios=Servicios.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})
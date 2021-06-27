from django.shortcuts import render,HttpResponse
from servicios.models import Servicios

# Create your views here.

def home(request):

    return render(request, "UPWapp/home.html")



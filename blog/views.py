from django.shortcuts import render,HttpResponse
from blog.models import Categorias, Post

# Create your views here.

def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html",{"posts": posts})

def categoria(request, categoria_id):

    categoria=Categorias.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"blog/categorias.html",{'categoria':categoria,'posts':posts})
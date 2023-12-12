from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from blog.models import blogPost

def home_page(request):
    qs = blogPost.objects.all()[:5]
    context = {"title": "Bienvenido - Comisiones DACyTI", 'blog_list': qs}
    return render(request, "index.html", context)

def about_page(request):
    return render(request, "about.html",{"title" : "Sobre nosotros"})

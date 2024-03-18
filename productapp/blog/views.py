from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import admin
# Create your views here.


def index(request):
    return render(request ,"blog/index.html")


def blogs( request):
    return render(request , "blog/blogs.html")

def blog_detail(request,id):
    return render("blog details: "+str(id))
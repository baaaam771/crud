from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'functioncrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'functioncrud/funccrud.html', {'blogs':blogs})

def create(request):
    return

def update(request):
    return

def delete(request):
    return

# Create your views here.

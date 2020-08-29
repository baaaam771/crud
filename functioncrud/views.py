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
    #새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        #입력한 블로그 글들을 저장해라
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    #글쓰기 페이지를 띄워주는 역할 == GET(!POST)
    else:
        # 단순히 입력받을 수 있는 form을 띄워줘라
        form =NewBlog()
        return render(request, 'functioncrud/new.html', {'form':form})

def update(request):
    return

def delete(request):
    return

# Create your views here.

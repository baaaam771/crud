from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView #데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터 추가
from .models import ClassBlog

class BlogView(ListView):           #html 템플릿 : 블로그 리스트를 담은 html =(소문자 모델)_list.html
    #template_name = 'classcrud/list.html'
    #context_object_name = 'blog_list'(object_list 말고 다른 이름)
    model = ClassBlog
    #ClassBlog로 만들어진 객체들을 달라

class BlogCreate(CreateView):       #html : form(입력공간)을 갖고 있는 html =(소문자 모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    #form에 들어가는 필드
    success_url = reverse_lazy('list')
    #성공했을때 redirect 같은 역할

class BlogDetail(DetailView):       #html : 상세 페이지를 담은 html =(소문자 모델)_detail.html
    #context_object_name = 'blogpost'(object 말고 다른 이름)
    model = ClassBlog

class BlogUpdate(UpdateView):       #html : form(입력공간)을 갖고 있는 html =(소문자 모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):       #html : 진짜로 지울 것인지 체크 =(소문자 모델)_confirm_delete.html
    model = ClassBlog
    success_url =reverse_lazy('list')



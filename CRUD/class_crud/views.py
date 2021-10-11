from typing import List
from django.shortcuts import render

from django.urls import reverse_lazy
from .models import ClassBlog
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class BlogView(ListView):
    template_name = 'class_crud/list.html'  #default html 이름 변경가능
    context_object_name = 'blog_list'   #default object 이름 변경 가능
    model = ClassBlog

class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):
    model = ClassBlog

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')
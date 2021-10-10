from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from django.utils import timezone


def home(request):
    blog = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blog})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details' : details})

def write(request):
    return render(request, 'write.html' )

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
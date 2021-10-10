from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

def home(request):
    blog = Blog.objects #쿼리셋
    #블로그의 모든 글을 대상
    blog_list = blog.all()
    #객체 3개당 한 페이지로 취급
    paginator = Paginator(blog_list, 2)
    #request된 페이지를 변수에 저장
    page = request.GET.get('page')
    #변수에 저장한 page를 return
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blog, 'posts':posts})

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

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
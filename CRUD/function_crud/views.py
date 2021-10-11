from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .form import NewBlog

# Create your views here.
def welcome(request):
    return render(request, 'function_crud/index.html')

def read(request):
    all_data = Blog.objects.all()
    return render(request, 'function_crud/funccrud.html', {'blogs':all_data})

def create(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'function_crud/new.html', {'form':form})
    return

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = NewBlog(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'function_crud/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')
from django.shortcuts import get_object_or_404, render
from .models import Blog

def home(request):
    blog = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blog})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details' : details})

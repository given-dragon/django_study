from django.shortcuts import get_object_or_404, render
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects    #모델로부터 전달받은 객체 = 쿼리셋이라고함
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})
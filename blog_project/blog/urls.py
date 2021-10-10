from django.urls import path
import blog.views

urlpatterns = [
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    path('write/', blog.views.write, name='write'),
    path('create/', blog.views.create, name='create'),
    path('newblog/', blog.views.blogpost, name='newblog'),
] 

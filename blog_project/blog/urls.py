from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.home, name='home'),
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    path('write/', blog.views.write, name='write'),
    path('create/', blog.views.create, name='create'),
] 

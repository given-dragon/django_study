from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__'   #모든 항목을 입력받으려면 이렇게
        fields = ['title', 'body']

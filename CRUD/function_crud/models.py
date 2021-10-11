from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title
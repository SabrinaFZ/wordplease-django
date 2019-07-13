from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):

    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=30)
    header = models.CharField(max_length=30)
    body = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category')
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
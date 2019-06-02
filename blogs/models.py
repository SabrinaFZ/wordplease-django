from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=30)
    header = models.CharField(max_length=30)
    body = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
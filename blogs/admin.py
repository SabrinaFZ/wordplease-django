from django.contrib import admin

# Register your models here.
from blogs.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
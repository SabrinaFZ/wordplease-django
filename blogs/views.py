from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views import View
from django.views.generic import ListView

from blogs.forms import PostForm
from blogs.models import Post, Blog


class LatestPostsView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-creation_date')

        context = {
            'latest_posts': posts
        }

        html = render(request, 'blogs/latest.html', context)

        return HttpResponse(html)


class BlogsListView(ListView):

    model = Blog
    template_name = 'blogs/list_blogs.html'


class BlogDetailView(View):

    def get(self, request, username):
        owner = get_object_or_404(User, username=username)
        posts = Post.objects.filter(owner = owner).order_by('-creation_date')

        context = {
            'blog_owner': owner,
            'blogs_posts': posts
        }

        html = render(request, 'blogs/blog_detail.html', context)

        return HttpResponse(html)


class PostDetailView(View):

    def get(self, request, username, pk):
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk)

        context = {
            'post': post
        }

        html = render(request, 'blogs/post_detail.html', context)

        return HttpResponse(html)


class NewPostView(LoginRequiredMixin, View):

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_post.pk))
            form = PostForm()

        context = {'form': form }
        return render(request, 'blogs/new_post.html', context)

    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/new_post.html', context)
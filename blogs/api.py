from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response

from blogs.permissions import PostPermission
from blogs.serializers import BlogListSerializer, PostListSerializer, PostSerializer, WritePostSerializer
from blogs.models import Post, Blog


class BlogViewSet(ModelViewSet):

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['owner__username']
    ordering_fields = ['name']
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class BlogDetailViewSet(GenericViewSet):

    permission_classes =  [PostPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'creation_date']

    def retrieve(self, request, pk):
        queryset = Post.objects.filter(blog=pk).order_by('-creation_date')

        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif not request.user.is_authenticated or request.user.username != getattr(Blog.objects.get(pk=pk), 'owner').username:
            serializer = PostListSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class PostAPIViewSet(GenericViewSet):

    permission_classes = [PostPermission]

    def create(self, request):
        request_copy = request.data.copy()
        request_copy['owner'] = request.user.id
        serializer = WritePostSerializer(data=request_copy)

        if serializer.is_valid():
            new_post = serializer.save()
            post_serializer = WritePostSerializer(new_post)
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        queryset = Post.objects.get(pk=pk)
        self.check_object_permissions(request, queryset)
        if queryset:
            serializer = WritePostSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        request_copy = request.data.copy()
        request_copy['owner'] = post.owner.id
        request_copy['blog'] = post.blog.id
        serializer = WritePostSerializer(post, data=request_copy)
        if serializer.is_valid():
            updated_post = serializer.save()
            user_serializer = PostSerializer(updated_post)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
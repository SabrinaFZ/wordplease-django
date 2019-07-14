from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from blogs.models import Blog, Post


class BlogListSerializer(ModelSerializer):

    url = serializers.SerializerMethodField('generate_url')

    def generate_url(self, obj):
        return '/blogs/' + obj.owner.username

    class Meta:
        model = Blog
        fields = ['id', 'name', 'url']


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'header', 'image', 'video', 'creation_date']


class WritePostSerializer(ModelSerializer):

    title = serializers.CharField()
    header = serializers.CharField()
    body = serializers.CharField()
    image = serializers.URLField(required=False)
    video = serializers.URLField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'header', 'image', 'video', 'body', 'blog', 'owner']

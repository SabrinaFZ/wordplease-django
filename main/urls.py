"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from blogs.views import LatestPostsView, BlogsListView, BlogDetailView, PostDetailView, NewPostView
from users.views import LoginView, LogoutView, SignUpView
from users.api import UsersViewSet
from blogs.api import BlogViewSet, BlogDetailViewSet, PostAPIViewSet

router = SimpleRouter()
router.register(r'blogs', BlogViewSet, basename='blogs_api')
router.register(r'blogs-detail', BlogDetailViewSet, basename='blogs_detail_api')
router.register(r'users', UsersViewSet, basename='users_api')
router.register(r'posts', PostAPIViewSet, basename='posts_api')


urlpatterns = [
    path('admin/', admin.site.urls),

    # api
    path('api/', include(router.urls)),

    # auth
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('sign-up', SignUpView.as_view(), name="sign_up"),

    # blogs
    path('blogs/', BlogsListView.as_view(), name="blogs"),
    path('blogs/<str:username>/', BlogDetailView.as_view(), name="blog_detail"),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name="post_detail"),

    # posts
    path('new-post', NewPostView.as_view(), name="new_post"),

    # home
    path('', LatestPostsView.as_view(), name="home"),

]

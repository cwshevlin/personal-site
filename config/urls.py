"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from config.views import home, toggle_dark_mode
from posts.views import posts, post_detail, posts_for_tag, tags, LatestPostsFeed
from .sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', home),
    path('dark-mode/', toggle_dark_mode),
    path('posts', posts),
    path('posts/<slug:slug>', post_detail),
    path('tags', tags),
    path('tags/<slug:tag>', posts_for_tag),
    path('admin/', admin.site.urls),
    path('feed/', LatestPostsFeed())
    path('sitemap.xml', sitemap,
         {'sitemaps': {
             'posts': PostSitemap,
             'static': StaticViewSitemap
         }},
         name='django.contrib.sitemaps.views.sitemap'),
]

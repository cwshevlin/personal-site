from django.contrib.sitemaps import Sitemap
from posts.models import Post
from datetime import datetime
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return Post.objects.exclude(deleted_at__lt=datetime.now()).order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/posts/{obj.slug}'


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['tags', 'posts']

    def location(self, obj):
        return reverse(obj)

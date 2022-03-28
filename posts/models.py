from django.db import models
from config import settings

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    description = models.CharField(max_length=255, default="A blog post.")
    slug = models.SlugField(max_length=128, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return f"/posts/{self.slug}"

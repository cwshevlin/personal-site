from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Post
from taggit.models import Tag
from config.views import is_dark_mode_processor
import markdown
from datetime import datetime


def posts(request):
    all_posts = Post.objects.exclude(deleted_at__lt=datetime.now()).order_by('-created_at')
    context = {**{'posts': all_posts}, **is_dark_mode_processor(request)}
    return render(request, 'posts.html', context)


def posts_for_tag(request, tag):
    tag = tag.replace('-', ' ')
    posts_with_tag = Post.objects.exclude(deleted_at__lt=datetime.now()).filter(tags__name__in=[tag])
    context = {**{'posts': posts_with_tag}, **is_dark_mode_processor(request)}
    return render(request, 'posts.html', context)


def tags(request):
    post_tags = Tag.objects.order_by('name')
    context = {**{'tags': post_tags}, **is_dark_mode_processor(request)}
    return render(request, 'tags.html', context)


def post_detail(request, slug):
    try:
        post = Post.objects.exclude(deleted_at__lt=datetime.now()).get(slug=slug)
    except Post.DoesNotExist:
        return Http404(f'Not found: {slug}')
    body = markdown.markdown(post.body)
    post_tags = post.tags.all()
    context = {**{'post': post, 'body': body, 'tags': post_tags}, **is_dark_mode_processor(request)}
    return render(request, 'post.html', context)



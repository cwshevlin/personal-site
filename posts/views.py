from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Post
from taggit.models import Tag
import markdown


def posts(request):
    all_posts = Post.objects.order_by('-created_at')
    return render(request, 'posts.html', {'posts': all_posts})


def posts_for_tag(request, tag):
    tag = tag.replace('-', ' ')
    posts_with_tag = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'posts.html', {'posts': posts_with_tag})


def tags(request):
    post_tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': post_tags})


def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Http404(f'Not found: {slug}')
    body = markdown.markdown(post.body)
    post_tags = post.tags.all()
    return render(request, 'tags.html', {'tags': post_tags})
    # return render(request, 'post.html', {'post': post, 'body': body, 'tags': post_tags})



from django.http import Http404
from django.shortcuts import render
from .models import Post
import markdown


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': all_posts})


def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Http404(f'Not found: {slug}')
    body = markdown.markdown(post.body)
    return render(request, 'post.html', {'post': post, 'body': body})

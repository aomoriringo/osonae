from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def home(request):
    not_consumed_posts = Post.not_consumed_posts(request.user).order_by('created_at')
    context = {'posts': not_consumed_posts}
    return render(request, 'home/index.html', context)

@login_required
def received(request):
    not_consumed_posts = Post.not_consumed_posts(request.user).order_by('created_at')
    received_posts     = Post.received_posts(request.user).order_by('created_at')
    liked_posts        = Post.liked_posts(request.user).order_by('created_at')
    context = {'received_posts'    : received_posts,
               'not_consumed_posts': not_consumed_posts,
               'liked_posts'       : liked_posts}
    return render(request, 'home/received.html', context)

@login_required
def posted(request):
    my_posts = Post.own_posts(request.user).order_by('created_at')
    context = {'posts': my_posts}
    return render(request, 'home/posted.html', context)


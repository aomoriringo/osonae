from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def home(request):
    return render(request, 'home/post.html')

@login_required
def received(request):
    context = {'received_posts'    : Post.received_posts(request.user),
               'not_consumed_posts': Post.not_consumed_posts(request.user),
               'liked_posts'       : Post.liked_posts(request.user)}
    return render(request, 'home/received.html', context)

@login_required
def posted(request):
    my_posts = Post.own_posts(request.user)
    context = {'posts': my_posts}
    return render(request, 'home/posted.html', context)


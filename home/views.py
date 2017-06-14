from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def home(request):
    not_consumed_posts = Post.objects.filter(feedback__owner=request.user
            ).filter(feedback__consumed=False
            ).order_by('created_at')
    context = {'posts': not_consumed_posts}
    return render(request, 'home/index.html', context)

@login_required
def posted(request):
    my_posts = Post.objects.filter(owner=request.user).order_by('created_at')
    context = {'posts': my_posts}
    return render(request, 'home/posted.html', context)

# def following(requests, screen_name):
#     return HttpResponse(f'{screen_name} following')
#
# def followers(requests, screen_name):
#     return HttpResponse(f'{screen_name} followers')



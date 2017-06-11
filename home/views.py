from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def home(request):
    return render(request, 'home/index.html')

def posted(request):
    posted = Post.objects.filter(owner=request.user).order_by
    context = {'posted': posted}
    return render(request, 'home/posted.html', context)

# def following(requests, screen_name):
#     return HttpResponse(f'{screen_name} following')
#
# def followers(requests, screen_name):
#     return HttpResponse(f'{screen_name} followers')



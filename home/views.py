from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/index.html')

# def following(requests, screen_name):
#     return HttpResponse(f'{screen_name} following')
# 
# def followers(requests, screen_name):
#     return HttpResponse(f'{screen_name} followers')



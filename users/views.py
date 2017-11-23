from django.shortcuts import render
from django.http import HttpResponse

def home(request, screen_name):
    context = None
    return render(request, 'users/profile.html', context)

def following(requests, screen_name):
    return HttpResponse(f'{screen_name} following')

def followers(requests, screen_name):
    return HttpResponse(f'{screen_name} followers')

def dummy(request):
    return HttpResponse('fuck')


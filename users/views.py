from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import MyUser

def home(request, screen_name):
    users = MyUser.objects.filter(username=screen_name)
    if len(users) > 0:
        specified_user = users[0]
        context = {"specified_user": specified_user}
        return render(request, 'users/profile.html', context)
    else:
        return HttpResponse(f'そういう人はいない')

def following(requests, screen_name):
    return HttpResponse(f'{screen_name} following')

def followers(requests, screen_name):
    return HttpResponse(f'{screen_name} followers')

def dummy(request):
    return HttpResponse('fuck')


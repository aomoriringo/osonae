from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import MyUser

def home(request, screen_name):
    specified_user = MyUser.get_user_by_screen(screen_name)
    if specified_user:
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


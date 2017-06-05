from django.shortcuts import render
from .models import MyUser

def login(request):
    return render(request, 'accounts/login.html')

def profile(request):
    print(dir(request))
    return render(request, 'accounts/profile.html')

#def logout(request):
#    return render(request, 'accounts/logout.html')

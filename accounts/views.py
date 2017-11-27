from django.shortcuts import render
from .models import MyUser
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.update(request)
    return render(request, 'accounts/profile.html')

#def logout(request):
#    return render(request, 'accounts/logout.html')

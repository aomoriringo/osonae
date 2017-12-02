from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import MyUser
from posts.models import Post

mode_list = ["received", "liked", "posted"]

def profile(request, screen_name):
    return redirect('/users/' + screen_name + '/received')

def profile_received(request, screen_name):
    return _get_profile_response(request, screen_name, mode="received")

def profile_liked(request, screen_name):
    return _get_profile_response(request, screen_name, mode="liked")

def profile_posted(request, screen_name):
    return _get_profile_response(request, screen_name, mode="posted")

def _get_profile_response(request, screen_name, mode="received"):
    context = _get_profile_context(screen_name, mode)
    if context:
        return render(request, 'users/profile.html', context)
    else:
        return HttpResponse(f'そういう人はいない')

def _get_profile_context(screen_name, mode):
    user = MyUser.get_user_by_screen(screen_name)
    if (not user) or (mode not in mode_list):
        return {}
    context = {"mode"          :     mode,
               "specified_user":     user,
               "len_received_posts": Post.received_posts(user).count(),
               "len_liked_posts":    Post.liked_posts(user).count(),
               "len_own_posts":      Post.own_posts(user).count()}
    if mode == "received":
        context["posts"] = Post.received_posts(user)
    if mode == "liked":
        context["posts"] = Post.liked_posts(user)
    if mode == "posted":
        context["posts"] = Post.own_posts(user)
    return context

# def following(requests, screen_name):
#     return HttpResponse(f'{screen_name} following')
#
# def followers(requests, screen_name):
#     return HttpResponse(f'{screen_name} followers')

def users(request):
    users = MyUser.objects.all()
    context = {"users": users}
    return render(request, 'users/index.html', context)

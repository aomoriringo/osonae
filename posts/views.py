from django.shortcuts import render, redirect
from .models import Post, Feedback
from django.contrib.auth.decorators import login_required
from accounts.models import MyUser


@login_required
def post(request):
    if request.method == 'POST':
        params = request.POST
        target_user = MyUser.get_user_by_screen(params['target'])
        p = Post(owner   = request.user,
                 url     = params['url'],
                 comment = params['comment'])
        p.save()
        f = Feedback(post = p,
                     owner = target_user)
        f.save()
        return redirect('/posted/')
    else:
        return render(request, 'posts/post.html')

@login_required
def consume(request):
    if request.method == 'POST':
        params = request.POST


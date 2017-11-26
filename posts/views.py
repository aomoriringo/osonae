from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.http import JsonResponse
from accounts.models import MyUser
from posts.models import Post
from .models import Post, Feedback
from .forms import PostForm


class PostView(FormView):
    form_class = PostForm
    template_name = 'posts/post.html'
    success_url = '/posted/'

    def form_valid(self, form):
        form.save_post(self.request)
        return super(PostView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostView, self).dispatch(*args, **kwargs)

def post_detail(request, id):
    context = {'post': Post.get_post_by_id(id)}
    return render(request, 'posts/detail.html', context)

def toggle_like(request, id):
    p = Post.get_post_by_id(id)
    f = p.get_feedback_by_user(request.user)
    if request.method == 'POST':
        if f.status == Feedback.STATUS_NEUTRAL:
            f.status = Feedback.STATUS_LIKE
        else:
            f.status = Feedback.STATUS_NEUTRAL
        f.save()
    return JsonResponse({})

def toggle_consume(request, id):
    p = Post.get_post_by_id(id)
    f = p.get_feedback_by_user(request.user)
    if request.method == 'POST':
        f.consumed = (not f.consumed)
        f.save()
    return JsonResponse({})

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
        return redirect('/')

@login_required
def consume(request):
    if request.method == 'POST':
        params = request.POST


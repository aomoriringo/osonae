from django import forms
from .models import Post, Feedback
from accounts.models import MyUser

class PostForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput, required=True)
    url      = forms.URLField(widget=forms.URLInput, required=True)
    comment  = forms.CharField(widget=forms.TextInput, required=False)

    def clean_username(self):
        username = self.data.get('username')
        if not MyUser.get_user_by_screen(username):
            raise forms.ValidationError('Specified user is not found.')
        return username

    def save_post(self, request):
        username = self.cleaned_data['username']
        user = MyUser.get_user_by_screen(username)
        p = Post(owner   = request.user,
                 url     = self.cleaned_data['url'],
                 comment = self.cleaned_data['comment'])
        p.save()
        f = Feedback(post = p,
                     owner = user)
        f.save()


from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
        url(r'^login', views.login, name='login'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^logout', logout, {'next_page': '/accounts/login'}, name='logout'),
]

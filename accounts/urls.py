from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
        url(r'^login', views.login),
        url(r'^profile', views.profile),
        url(r'^logout', logout, name='logout'),
]

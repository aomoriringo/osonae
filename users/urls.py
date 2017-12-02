from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)$',          views.profile, name="profile"),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/received$', views.profile_received, name="received"),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/liked$',    views.profile_liked, name="liked"),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/posted$',   views.profile_posted, name="posted"),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/following$', views.following),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/followers$', views.followers),
        url(r'^$', views.users, name="index")
]

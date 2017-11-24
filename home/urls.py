from django.conf.urls import url, include
from . import views
from posts import views as post_views


urlpatterns = [
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)$', views.home),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/following$', views.following),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/followers$', views.followers)
        url(r'^post/$', post_views.post, name="post"),
        url(r'^received/$', views.received, name="received"),
        url(r'^posted/$', views.posted, name="posted"),
        url(r'^$', views.home, name="index")
]

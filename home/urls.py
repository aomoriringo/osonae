from django.conf.urls import url, include
from . import views
from posts.views import PostView

urlpatterns = [
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)$', views.home),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/following$', views.following),
        # url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/followers$', views.followers)
        url(r'^received/$', views.received, name="received"),
        url(r'^posted/$', views.posted, name="posted"),
        url(r'^$', PostView.as_view(), name="index"),
]

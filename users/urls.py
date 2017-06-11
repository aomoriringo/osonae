from django.conf.urls import url, include
from . import views

urlpatterns = [
        # url(r'^$', views.dummy),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)$', views.home),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/following$', views.following),
        url(r'^(?P<screen_name>[a-zA-Z0-9_]+)/followers$', views.followers)
]
from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^(?P<id>[0-9]+)/toggle_like$', views.toggle_like, name="toggle_like"),
        url(r'^(?P<id>[0-9]+)/toggle_consume$', views.toggle_consume, name="toggle_consume"),
        url(r'^(?P<id>[0-9]+)$', views.post_detail, name="detail"),
        url(r'^$', views.post, name="post"),
]

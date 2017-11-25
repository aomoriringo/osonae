from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^(?P<id>[0-9]+)$', views.post_detail, name="detail"),
        url(r'^$', views.post, name="post"),
]

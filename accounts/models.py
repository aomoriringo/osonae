# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.CharField(max_length=1000, default='')
    display_name = models.CharField(max_length=40, default='')
    icon_url = models.URLField('画像URL', blank=True)

    def update(self, request):
        params = request.POST
        # self.username = params['username']
        self.display_name = params['display_name']
        self.icon_url = params['icon_url']
        self.bio = params['bio']
        self.save()

    @classmethod
    def get_user_by_screen(cls, username):
        users = cls.objects.filter(username=username)
        if len(users) > 0:
            return users[0]
        else:
            return None

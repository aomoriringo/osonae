# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.CharField(max_length=1000, default='')
    icon_url = models.URLField('画像URL', blank=True)

    def update(self, request):
        params = request.POST
        self.username = params['username']
        self.icon_url = params['icon_url']
        self.bio = params['bio']
        self.save()

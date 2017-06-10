# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.CharField(max_length=1000, default='')
    image_url = models.URLField('画像URL', blank=True)


# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100)


#class MyUser(AbstractUser):
#    image_url = models.URLField('画像URL', blank=True)


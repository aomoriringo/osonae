# -*- coding: utf-8 -*-
from django.db import models
from accounts.models import MyUser

class Post(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def feedbacks(self):
        return Feedback.objects.filter(post__id = self.id)

    @property
    def receivers(self):
        return [x.owner for x in self.feedbacks]

class Feedback(models.Model):
    STATUS_NEUTRAL = 0
    STATUS_LIKE = 1
    FB_STATUS_CHOICES = (
        (STATUS_NEUTRAL, 'Neutral'),
        (STATUS_LIKE, 'Like')
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    consumed = models.BooleanField(default=False)
    status = models.IntegerField(
        choices = FB_STATUS_CHOICES,
        default = STATUS_NEUTRAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

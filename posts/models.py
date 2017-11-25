# -*- coding: utf-8 -*-
from django.db import models
from accounts.models import MyUser

class Post(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    url = models.URLField(max_length=500, blank=False)
    comment = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def own_posts(cls, user):
        return cls.objects.filter(owner=user)

    @classmethod
    def received_posts(cls, user):
        return cls.objects.filter(feedback__owner=user)

    @classmethod
    def consumed_posts(cls, user):
        return cls.received_posts(user).filter(feedback__consumed=True)

    @classmethod
    def not_consumed_posts(cls, user):
        return cls.received_posts(user).filter(feedback__consumed=False)

    @classmethod
    def liked_posts(cls, user):
        return cls.received_posts(user).filter(feedback__status=Feedback.STATUS_LIKE)

    @property
    def feedbacks(self):
        return Feedback.objects.filter(post = self)

    @property
    def receivers(self):
        return [x.owner for x in self.feedbacks]

    def get_feedback_by_user(self, user):
        feedbacks = self.feedbacks.filter(owner = user)
        if len(feedbacks) > 0:
            return feedbacks[0]
        else:
            None

    def is_consumed(self, user):
        feedback = self.get_feedback_by_user(user)
        if feedback:
            return feedback.consumed
        else:
            return False

    def is_liked(self, user):
        feedback = self.get_feedback_by_user(user)
        if feedback:
            return feedback.is_liked
        else:
            return False

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

    @property
    def is_liked(self):
        return self.status == Feedback.STATUS_LIKE


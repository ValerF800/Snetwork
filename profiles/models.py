from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to="profiles/%Y/%m/%d", default="default.jpg",blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    following = models.ManyToManyField('self', related_name='followers', blank=True, symmetrical=False)
    # subscribers = models.JSONField(null=True)
    # subscriptions = models.JSONField(null=True)




class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messages')
    body = models.TextField()
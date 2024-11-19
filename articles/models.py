from django.urls import reverse

from django.contrib.auth import get_user_model
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE, related_name='posts')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.id})


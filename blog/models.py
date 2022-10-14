from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    updatedDate = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, null = True, blank=True, on_delete = models.CASCADE)
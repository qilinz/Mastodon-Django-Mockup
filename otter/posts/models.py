from django.db import models
from users.models import CustomUser


class Post(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.ImageField(upload_to='uploads/%Y/%m', default=None)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    img_url = models.ImageField(upload_to='uploads/%Y/%m', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
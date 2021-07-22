from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_post(request, text):
        user = request.user
        post = Post(created_by=user, text=text)
        post.save()
        return post

    class Meta:
        app_label = 'user'


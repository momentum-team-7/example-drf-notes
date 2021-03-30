from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title

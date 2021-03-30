from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="notes")
    tags = models.ManyToManyField(to=Tag, related_name="notes", blank=True)

    def __str__(self):
        return self.title

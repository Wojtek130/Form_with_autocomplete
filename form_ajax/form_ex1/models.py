from unicodedata import name
from django.db import models
from django.utils import timezone
# Create your models here.

class LoginData(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_conf = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Login Data str"

class Movie(models.Model):
    title = models.TextField()

    def __str__(self) -> str:
        return f"Movie({self.title})"

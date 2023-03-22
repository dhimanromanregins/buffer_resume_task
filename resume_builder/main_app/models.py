from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    skill = models.TextField(max_length=10000)
    about_you = models.TextField(max_length=1000)
    previous_projects = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

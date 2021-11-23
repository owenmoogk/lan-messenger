from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=1000)
    owner = models.ForeignKey('auth.User', related_name='packages', on_delete=models.CASCADE, null=True)

admin.site.register(Message)
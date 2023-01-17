from django.db import models
from django import forms

class Server(models.Model):

    hostname = models.CharField(default='')
    username = models.CharField(default='')
    password = models.CharField(widget=forms.PasswordInput)



# Create your models here.

from django.db import models

class Server(models.Model):

    ip = models.CharField(default='', max_length=500)
    username = models.CharField(default='', max_length=500)
    password = models.CharField(default='', max_length=500)

# Create your models here.

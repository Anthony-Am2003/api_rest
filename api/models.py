from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    is_activate = models.BooleanField(default=True)
    

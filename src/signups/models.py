from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    
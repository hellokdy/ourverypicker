from django.db import models
from django.contrib.auth.models import User
# from landing.views import inputtext

# Create your models here.

class landing(models.Model):
  
    # author = models.CharField(max_length=100)
    inputtext = models.TextField()
    
    def __str__(self):
      return f'{self.inputtext}'
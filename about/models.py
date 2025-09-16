from django.db import models
from django.contrib.auth.models import User # Import models to connect

# Create your models here.
    
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
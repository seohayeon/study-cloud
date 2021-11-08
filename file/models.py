from django.db import models

# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=10)
    file = models.CharField(max_length=100)
    extension = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Category(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
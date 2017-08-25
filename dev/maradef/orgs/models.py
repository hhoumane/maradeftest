from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(default='',max_length=200)
    location = models.CharField(default='',max_length=10)
    website = models.URLField(default='',verbose_name="URL")
    Description = models.CharField(default='',max_length=200)
    

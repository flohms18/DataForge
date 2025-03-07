from django.db import models

# Create your models here.

class DataCareer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True, null=True)
    
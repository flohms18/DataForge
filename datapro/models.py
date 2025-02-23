from django.db import models

# Create your models here.



class DataJob(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tools = models.JSONField()
    
from django.db import models

# Create your models here.

class DataProfession(models.Model):
    DataProName = models.CharField(max_length=200)
    DataProDescription = models.CharField(max_length=600)
    DataProTools = models.CharField(max_length=200)
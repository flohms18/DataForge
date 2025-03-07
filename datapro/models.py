from django.db import models

# Create your models here.

class DataCareer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    published_date = models.DateTimeField(auto_now_add=True)
    
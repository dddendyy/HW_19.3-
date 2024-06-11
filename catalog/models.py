from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(null=True, blank=True)
    manufactured_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

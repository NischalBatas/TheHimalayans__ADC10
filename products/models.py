from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.TextField()
    product_price=models.FloatField()
    product_category=models.TextField()
    product_image=models.ImageField()
pip install django

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class ARSession(models.Model):
    user_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Add more fields as needed, e.g., placement, scale, orientation, etc.

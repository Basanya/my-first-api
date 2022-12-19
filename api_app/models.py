from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_length=100, max_digits=7, decimal_places=2)
    stock = models.CharField(max_length=100)
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.name

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    
    def __str__(self):
        return self.name
    
    

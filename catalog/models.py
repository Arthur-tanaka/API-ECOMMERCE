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
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=2, choices=[('ML', 'Masculino'), ('FM', 'Feminino'), ('UN', 'Unissex')])
    imagem = models.ImageField(upload_to='product_images/')

    
    def __str__(self):
        return self.name
    
    

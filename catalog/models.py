from django.db import models

from django.conf import settings

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
    
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.product is not None:
            return f"A quantidade de {self.product.name} é {self.quantity}"
        else:
            return f"Produto removido"

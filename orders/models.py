from django.db import models
from django.conf import settings
from catalog.models import Product

#Ainda vou corrigir o relacionamento do cliente com o pedido.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pendente', choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('cancelado', 'Cancelado')])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        if self.product is not None:
            return f"A quantidade de {self.product.name} é {self.quantity}"
        else:
            return f"Produto removido"


from django.db import models

#Ainda vou corrigir o relacionamento do cliente com o pedido.
class Order(models.Model):
    cliente_id = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('processando', 'Processando'), ('concluido', 'Concluído')])
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100, unique=True)

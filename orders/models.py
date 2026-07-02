from django.db import models
from users.models import CustomUser
from products.models import Product

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'En attente'
    CONFIRMED = 'confirmed', 'Confirmée'
    PROCESSING = 'processing', 'En traitement'
    SHIPPED = 'shipped', 'Expédiée'
    DELIVERED = 'delivered', 'Livrée'
    CANCELLED = 'cancelled', 'Annulée'

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    total = models.FloatField()
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default='pending')
    adresse = models.JSONField()
    reference = models.CharField(max_length=50, unique=True, blank=True, null=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'orders'
        
    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'order_items'
        
    def __str__(self):
        return f"{self.product.nom} x {self.quantite}"

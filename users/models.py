from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('vendeur', 'Vendeur'),
        ('admin', 'Admin'),
    )
    
    telephone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    adresse = models.JSONField(default=dict, blank=True)
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.email

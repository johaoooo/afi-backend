from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=500, blank=True, null=True, help_text="URL Cloudinary de l'image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        
    def __str__(self):
        return self.nom

class Product(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    prix_promo = models.FloatField(blank=True, null=True)
    images = models.JSONField(default=list, help_text="Liste des URLs Cloudinary des images")
    stock = models.IntegerField(default=0)
    note = models.FloatField(default=0)
    avis = models.IntegerField(default=0)
    caracteristiques = models.JSONField(default=dict, blank=True)
    est_disponible = models.BooleanField(default=True)
    est_populaire = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'products'
        
    def __str__(self):
        return self.nom

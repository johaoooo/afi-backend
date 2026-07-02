from rest_framework import serializers
from .models import Product, Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'slug', 'description', 'image', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.CharField(source='categorie.nom', read_only=True)
    categorie_slug = serializers.CharField(source='categorie.slug', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'nom', 'description', 'prix', 'prix_promo',
            'images', 'stock', 'note', 'avis', 'caracteristiques',
            'est_disponible', 'est_populaire',
            'categorie', 'categorie_nom', 'categorie_slug',
            'created_at', 'updated_at'
        ]

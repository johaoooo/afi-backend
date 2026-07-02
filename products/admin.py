from django.contrib import admin
from .models import Product, Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug', 'created_at')
    search_fields = ('nom', 'description')
    prepopulated_fields = {'slug': ('nom',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'stock', 'est_disponible', 'categorie')
    list_filter = ('est_disponible', 'categorie')
    search_fields = ('nom', 'description')

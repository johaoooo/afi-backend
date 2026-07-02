from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Categorie
from .serializers import ProductSerializer, CategorieSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie__slug', 'est_disponible', 'est_populaire']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]  # ✅ Permet la lecture sans authentification
    
    @action(detail=False, methods=['get'])
    def populaires(self, request):
        produits = Product.objects.filter(est_populaire=True, est_disponible=True)[:10]
        serializer = self.get_serializer(produits, many=True)
        return Response(serializer.data)

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]  # ✅ Permet la lecture sans authentification

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import HeroSlide, HeroStat, AboutContent, FeatureBlock, Artisan, Testimonial, Partner
from .serializers import (
    HeroSlideSerializer, HeroStatSerializer, AboutContentSerializer, 
    FeatureBlockSerializer, ArtisanSerializer, TestimonialSerializer, PartnerSerializer
)

class HeroSlideViewSet(viewsets.ModelViewSet):
    queryset = HeroSlide.objects.filter(is_active=True)
    serializer_class = HeroSlideSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class HeroStatViewSet(viewsets.ModelViewSet):
    queryset = HeroStat.objects.filter(is_active=True)
    serializer_class = HeroStatSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class AboutContentViewSet(viewsets.ModelViewSet):
    queryset = AboutContent.objects.filter(is_active=True)
    serializer_class = AboutContentSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class FeatureBlockViewSet(viewsets.ModelViewSet):
    queryset = FeatureBlock.objects.filter(is_active=True)
    serializer_class = FeatureBlockSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = Artisan.objects.filter(is_active=True)
    serializer_class = ArtisanSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(is_active=True)
    serializer_class = PartnerSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

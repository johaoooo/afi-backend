from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategorieViewSet
from services.views import ServiceViewSet
from formations.views import FormationViewSet
from contact_messages.views import ContactMessageViewSet
from content.views import (
    HeroSlideViewSet, HeroStatViewSet, AboutContentViewSet, 
    FeatureBlockViewSet, ArtisanViewSet, TestimonialViewSet, PartnerViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategorieViewSet)
router.register('services', ServiceViewSet)
router.register('formations', FormationViewSet)
router.register('contact-messages', ContactMessageViewSet)
router.register('hero-slides', HeroSlideViewSet)
router.register('hero-stats', HeroStatViewSet)
router.register('about', AboutContentViewSet)
router.register('features', FeatureBlockViewSet)
router.register('artisans', ArtisanViewSet)
router.register('testimonials', TestimonialViewSet)
router.register('partners', PartnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

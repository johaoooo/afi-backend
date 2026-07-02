from rest_framework import serializers
from .models import HeroSlide, HeroStat, AboutContent, FeatureBlock, Artisan, Testimonial, Partner

class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = ['id', 'image', 'title', 'subtitle', 'description', 'button_text', 'button_link', 'order', 'is_active']

class HeroStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStat
        fields = ['id', 'value', 'label', 'icon', 'order', 'is_active']

class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = ['id', 'title', 'subtitle', 'description', 'image', 'badge_text', 'badge_value', 'is_active']

class FeatureBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureBlock
        fields = ['id', 'title', 'subtitle', 'description', 'icon', 'button_text', 'button_link', 'is_dark', 'order', 'is_active']

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = ['id', 'name', 'specialty', 'gender', 'location', 'experience', 'description', 'achievements', 'order', 'is_active']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'city', 'text', 'rating', 'order', 'is_active']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo', 'description', 'website', 'order', 'is_active']

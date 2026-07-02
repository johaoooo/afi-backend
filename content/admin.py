from django.contrib import admin
from .models import HeroSlide, HeroStat, AboutContent, FeatureBlock, Artisan, Testimonial, Partner

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Contenu', {
            'fields': ('image', 'title', 'subtitle', 'description', 'button_text', 'button_link')
        }),
        ('Ordre & statut', {
            'fields': ('order', 'is_active')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(HeroStat)
class HeroStatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('label',)

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    fieldsets = (
        ('Contenu principal', {
            'fields': ('title', 'subtitle', 'description', 'image')
        }),
        ('Badge', {
            'fields': ('badge_text', 'badge_value')
        }),
        ('Statut', {
            'fields': ('is_active',)
        }),
    )

@admin.register(FeatureBlock)
class FeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_dark', 'is_active')
    list_editable = ('order', 'is_dark', 'is_active')
    search_fields = ('title', 'description')

@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'gender', 'location', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'specialty', 'location')
    list_filter = ('gender', 'is_active')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'city', 'text')
    list_filter = ('rating', 'is_active')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'description')

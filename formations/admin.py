from django.contrib import admin
from .models import Formation

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('name', 'duree', 'niveau', 'places', 'date')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

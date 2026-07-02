from django.db import models

class Formation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=500, blank=True, null=True, help_text="URL Cloudinary de l'image")
    duree = models.CharField(max_length=50, blank=True)
    niveau = models.CharField(max_length=50, blank=True)
    places = models.IntegerField(default=0)
    date = models.CharField(max_length=50, blank=True)
    details = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'formations'
        
    def __str__(self):
        return self.name

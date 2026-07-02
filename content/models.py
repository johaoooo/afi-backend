from django.db import models

class HeroSlide(models.Model):
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, help_text="Description affichée entre le sous-titre et les boutons")
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hero_slides'
        ordering = ['order']

    def __str__(self):
        return self.title or f"Slide {self.id}"

class HeroStat(models.Model):
    value = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, help_text="Nom de l'icône (FiUsers, FiShoppingBag, etc.)")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'hero_stats'
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.label}"

class AboutContent(models.Model):
    title = models.CharField(max_length=200, default="L'artisanat africain à son meilleur.")
    subtitle = models.CharField(max_length=100, default="À propos de nous")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    badge_text = models.CharField(max_length=50, blank=True, default="100% Authentique & fait main")
    badge_value = models.CharField(max_length=20, blank=True, default="100%")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'about_content'
        verbose_name_plural = "About content"

    def __str__(self):
        return "À propos" if self.is_active else "À propos (inactif)"

class FeatureBlock(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='FiStar')
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.CharField(max_length=200, blank=True)
    is_dark = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feature_blocks'
        ordering = ['order']

    def __str__(self):
        return self.title

class Artisan(models.Model):
    GENDER_CHOICES = (
        ('male', 'Homme'),
        ('female', 'Femme'),
    )
    
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='female')
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=50, help_text="Ex: 15 ans")
    description = models.TextField(blank=True)
    achievements = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'artisans'
        ordering = ['order']

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, f"{i} étoiles") for i in range(1, 6)])
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'testimonials'
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.city}"

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'partners'
        ordering = ['order']

    def __str__(self):
        return self.name

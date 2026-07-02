from django.db import models

class MessageStatus(models.TextChoices):
    UNREAD = 'unread', 'Non lu'
    READ = 'read', 'Lu'
    REPLIED = 'replied', 'Répondu'
    ARCHIVED = 'archived', 'Archivé'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=MessageStatus.choices, default='unread')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'contact_messages'
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.name} - {self.subject or 'Sans sujet'}"

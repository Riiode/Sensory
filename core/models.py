from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_type  = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file        = models.FileField(upload_to='uploads/')
    thumbnail   = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']
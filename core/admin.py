from django.contrib import admin
from .models import MediaItem, Category

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'category', 'uploaded_at']
    list_filter  = ['media_type', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
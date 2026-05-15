from django.shortcuts import render, get_object_or_404
from .models import MediaItem, Category

def home(request):
    featured = MediaItem.objects.all()[:6]
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'featured': featured,
        'categories': categories,
    })

def gallery(request):
    media_type = request.GET.get('type', '')
    category_id = request.GET.get('category', '')
    items = MediaItem.objects.all()

    if media_type:
        items = items.filter(media_type=media_type)
    if category_id:
        items = items.filter(category_id=category_id)

    return render(request, 'core/gallery.html', {
        'items': items,
        'categories': Category.objects.all(),
        'selected_type': media_type,
        'selected_category': category_id,
    })

def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    related = MediaItem.objects.filter(media_type=item.media_type).exclude(pk=pk)[:4]
    return render(request, 'core/detail.html', {'item': item, 'related': related})
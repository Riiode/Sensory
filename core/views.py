from django.shortcuts import render, get_object_or_404
from .models import MediaItem, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm, MediaUploadForm

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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def upload(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.uploaded_by = request.user
            item.save()
            messages.success(request, 'Upload successful!')
            return redirect('media_detail', pk=item.pk)
    else:
        form = MediaUploadForm()
    return render(request, 'core/upload.html', {'form': form})
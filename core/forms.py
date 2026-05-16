from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MediaItem

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'media_type', 'file', 'thumbnail', 'category']
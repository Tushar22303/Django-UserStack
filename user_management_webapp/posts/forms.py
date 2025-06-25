from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter post title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 5,
                'placeholder': 'Write your post description...',
            }),
        }
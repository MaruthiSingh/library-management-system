from django import forms
from .models import Book

class BookEntryForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'isbn', 'published_year', 'available_copies', 'description', 'cover_image']

    # Custom styling using widgets
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter book title'
        })
    )

    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter author name'
        })
    )

    category = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter category'
        })
    )

    isbn = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter ISBN number'
        })
    )

    published_year = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter published year'
        })
    )

    available_copies = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter available copies'
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md h-12',
            'placeholder': 'Enter description'
        })
    )

    cover_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
        })
    )

class UserInfoForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter your email'
        })
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input py-3 px-4 border-gray-300 border-4 rounded-md',
            'placeholder': 'Enter your phone number (optional)'
        })
    )
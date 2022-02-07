from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contactForm',
        'placeholder': 'Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'contactEmail',
        'placeholder': 'Email'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contactSubject',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'contactMessage',
        'placeholder': 'Message'
    }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

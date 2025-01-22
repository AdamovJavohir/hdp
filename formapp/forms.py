from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'age', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Yoshingiz'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }

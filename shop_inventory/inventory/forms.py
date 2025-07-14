from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model  = Item
        fields = ['name', 'price', 'quantity', 'category']
        widgets = {
            'price':    forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': '0'}),
        }
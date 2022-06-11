from django import forms
from django.forms import ModelForm

from drug_store.models import Product, Category


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'description', 'price', 'available', 'stock']
        widgets = {
            'category': forms.Select(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.TextInput(attrs={"class": "form-control"}),
        }


class NewCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [ 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.TextInput(attrs={"class": "form-control"}),
        }

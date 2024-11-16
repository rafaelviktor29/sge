from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'brand',
            'category',
            'description',
            'serie_number',
            'cost_price',
            'selling_price'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'brand': 'Marca',
            'category': 'Categoria',
            'description': 'Descrição',
            'serie_number': 'Número de série',
            'cost_price': 'Preço de custo',
            'selling_price': 'Preço de venda'
        }

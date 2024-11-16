from django import forms
from django.core.exceptions import ValidationError
from .models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if quantity <= 0:
            raise ValidationError(
                'A quantidade de entrada deve ser maior que 0.'
            )

        return quantity

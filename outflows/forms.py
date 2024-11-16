from django import forms
from django.core.exceptions import ValidationError
from .models import Outflow


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade em estoque de {product.title} é de {product.quantity} unidades.'
            )
        elif quantity <= 0:
            raise ValidationError(
                'A quantidade de saída deve ser maior que 0.'
            )

        return quantity

from django.forms import ModelForm, fields, widgets
from ..models import Product
from django.forms.widgets import NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description',
                  'cantidad', 'unity', 'category', 'brand']
        widgets = {
            'cantidad': NumberInput(attrs={'min': 0}),
            'price': NumberInput(attrs={'min': 0})
        }

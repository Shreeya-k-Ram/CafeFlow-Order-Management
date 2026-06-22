from django import forms
from .models import Order
from .models import MenuItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'menu_item', 'quantity']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['menu_item'].queryset = MenuItem.objects.filter(available=True)

from django import forms

from marketplace.models import CartItem

class AddItemToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = [
            'quantity'
        ]
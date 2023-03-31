from django import forms
from seller.models import Seller
from marketplace.models import Product

class SellerRegisterationForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'name',
            'phone',
            'email'
        ]

        labels = {
            'name': 'Business name',
            'phone': 'Business Phone number',
            'email': 'Business email'
        }

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'quantity'
        ]
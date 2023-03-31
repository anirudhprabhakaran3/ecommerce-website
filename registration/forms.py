from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.models import User, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'mobile_no',
        )

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'address',
            'city',
            'state',
            'pincode',
        )
from django.contrib.auth.forms import UserCreationForm
from registration.models import User

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
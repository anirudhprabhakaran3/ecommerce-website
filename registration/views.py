from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from registration.forms import CustomUserCreationForm
from marketplace.models import Cart

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            cart = Cart(user=user)
            cart.save()
            messages.success(request, "Registered successfully!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    args = {
        'form': form
    }
    return render(request, 'registration/signup.html', args)
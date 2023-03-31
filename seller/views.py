from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from seller.forms import SellerRegisterationForm, AddProductForm
from marketplace.models import Product

# Create your views here.

@login_required
def register(request):
    if hasattr(request.user, 'seller'):
        messages.error(request, "Seller profile already exists!")
        return redirect('seller_profile')
    if request.method == "POST":
        form = SellerRegisterationForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            messages.success(request, "Registered seller successfully!")
            redirect('home')
        else:
            messages.error(request, "Error registering seller!")
            return redirect('seller_register')
    else:
        form = SellerRegisterationForm()
    args = {
        'form': form,
    }
    return render(request, 'seller/register.html', args)

@login_required
def profile(request):
    if not hasattr(request.user, 'seller'):
        messages.error(request, "Please make a seller profile first!")
        return redirect('seller_register')
    products = Product.objects.filter(seller=request.user.seller)
    args = {
        'products': products,
    }
    return render(request, 'seller/profile.html', args)

@login_required
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect('seller_profile')
        else:
            messages.error(request, "Error adding product!")
            return redirect('add_product')
    else:
        form = AddProductForm()
    args = {
        'form': form
    }
    return render(request, 'seller/add_product.html', args)

@login_required
def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('seller_profile')
        else:
            messages.error(request, "Error updating product!")
            return redirect('update_product', id=id)
    else:
        form = AddProductForm(instance=product)
    args = {
        'form': form,
        'product': product,
    }
    return render(request, 'seller/update_product.html', args)

@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id)

    if product.seller != request.user.seller:
        messages.error(request, "You don't have permission to delete this product!")
        return redirect('seller_profile')

    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('seller_profile')
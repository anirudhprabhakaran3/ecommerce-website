from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

from marketplace.models import Product, Cart, CartItem
from marketplace.forms import AddItemToCartForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    args = {
        'products': products,
    }
    return render(request, "marketplace/home.html", args)

@login_required
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user.id)
    if request.method == "POST":
        form = AddItemToCartForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            if cart_item.quantity > product.quantity:
                messages.error(request, "Not enough items in stock!")
                return redirect('view_product', product_id=product_id)
            cart_item.cart = cart
            cart_item.product = product
            cart_item.total_price = cart_item.quantity * product.price
            cart_item.save()
            messages.success(request, "Item added to cart!")
            return redirect('view_product', product_id=product_id)
        else:
            messages.error(request, "Invalid form")
            return redirect('view_product', product_id=product_id)
    else:
        form = AddItemToCartForm()
    args = {
        'product': product,
        'form': form,
    }
    return render(request, "marketplace/product.html", args)

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    grand_total = cart_items.aggregate(Sum('total_price'))
    args = {
        'cart': cart,
        'cart_items': cart_items,
        'grand_total': grand_total['total_price__sum'],
    }

    return render(request, 'marketplace/view_cart.html', args)

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart = cart_item.cart
    if cart.user != request.user:
        messages.error(request, "You do not have permission to do that!")
        return redirect('view_cart')
    cart_item.delete()
    messages.success(request, "Item removed from cart!")
    return redirect('view_cart')
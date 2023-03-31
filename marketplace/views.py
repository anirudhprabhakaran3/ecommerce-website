from django.shortcuts import render

from marketplace.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    args = {
        'products': products,
    }
    return render(request, "marketplace/home.html", args)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    args = {
        'product': product,
    }
    return render(request, "marketplace/product.html", args)
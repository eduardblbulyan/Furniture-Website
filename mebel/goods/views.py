from django.shortcuts import render
from .models import Categories, Product

def catalog(request):
    goods = Product.objects.all()
    context = { # temporary mock db emulation
        'title': 'Home - Catalog',
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


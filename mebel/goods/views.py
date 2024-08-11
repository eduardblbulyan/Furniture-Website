from django.shortcuts import render
from .models import Categories, Product

def catalog(request):
    goods = Product.objects.all()
    context = { # temporary mock db emulation
        'title': 'Home - Catalog',
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    categories = Categories.objects.all()
    return render(request, "goods/product.html", {"categroies": categories})


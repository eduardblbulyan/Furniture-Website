from django.shortcuts import render, get_list_or_404
from .models import Categories, Product

def catalog(request, category_slug):
    if category_slug=="all":
        goods = Product.objects.all()
    else:
        # if not goods.exists():
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
        
    context = { # temporary mock db emulation
        'title': 'Home - Catalog',
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


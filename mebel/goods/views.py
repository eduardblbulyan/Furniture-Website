from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Categories, Product

def catalog(request, category_slug):
    
    page = int(request.GET.get('page', 1)) # if not `page` key, set default 1


    if category_slug=="all":
        goods = Product.objects.all()
    else:
        # if not goods.exists():
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
        
    context = { # temporary mock db emulation
        'title': 'Home - Catalog',
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Categories, Product

def catalog(request, category_slug):
    
    page = int(request.GET.get('page', 1)) # if not `page` key, set default 1
    on_sale = int(request.GET.get('on_sale', None)) # return None if no data
    order_by = int(request.GET.get('order_by', None)) # get by name of input

    if category_slug=="all":
        goods = Product.objects.all()
    else:
        # if not goods.exists():
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by:
        goods = goods.order_by(order_by)

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


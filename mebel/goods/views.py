from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Categories, Product

from goods.utils import q_search

def catalog(request, category_slug=None):
    
    page = int(request.GET.get('page', 1)) # if not `page` key, set default 1
    on_sale = request.GET.get('on_sale', None) # return None if no data
    order_by = request.GET.get('order_by', None) # get by name of input
    query = request.GET.get("q", None)

    if category_slug=="all":
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        # if not goods.exists():
        goods = Product.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
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


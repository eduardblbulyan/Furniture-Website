from goods.models import Product

from django.db.models import Q

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]
    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token) # like += 
        q_objects |= Q(name__icontains=token)  

    return Product.objects.filter(q_objects)


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": "Some content about furnitures"
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")
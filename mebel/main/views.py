from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - О нас",
        "content": "Информация о магазине",
        "text_on_page": "Какой то текст!!", # avoid hyphens (-) because template can not understand text-on-page
        "categories": categories
    }
    return render(request, 'main/about.html', context)
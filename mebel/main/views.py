from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": "Home - О нас",
        "content": "Информация о магазине",
        "text_on_page": "Какой то текст!!" # avoid hyphens (-) because template can not understand text-on-page
    }
    return render(request, 'main/about.html', context)
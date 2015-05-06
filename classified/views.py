from django.shortcuts import render
from adverts.models import Category


def index(request):
    cats = Category.objects.all()
    c = {}
    c['cats'] = cats
    return render(request, 'index.html', c)


def error404(request):
    return render(request, '404.html')
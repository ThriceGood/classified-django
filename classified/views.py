from django.shortcuts import render
from adverts.models import Category


# index view, home page
def index(request):
    # get all categories and add to dict
    cats = Category.objects.all()
    c = {}
    c['cats'] = cats
    # render index template and pass in context dict (categories)
    return render(request, 'index.html', c)


# currently not used
def error404(request):
    return render(request, '404.html')
from django.shortcuts import render

from mainapp.models import Product

def index(request):
    title = 'Главная страница'

    prods = Product.objects.all()[:2]

    context = {
        'title': title,
        'products': prods,
    }


    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
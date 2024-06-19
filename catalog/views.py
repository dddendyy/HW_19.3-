from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def products(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'catalog/products_list.html', context)

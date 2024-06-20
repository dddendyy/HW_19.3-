from django.shortcuts import render, get_object_or_404

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


def product_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_card.html', context)

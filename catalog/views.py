from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# Create your views here.


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'


class ProductCardDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'


# def contacts(request):
#     return render(request, 'catalog/contacts.html')


# def home(request):
#     return render(request, 'catalog/home.html')


# def products(request):
#     product_list = Product.objects.all()
#     context = {'product_list': product_list}
#     return render(request, 'catalog/products_list.html', context)


# def product_card(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_card.html', context)

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

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ProductsListView(ListView):
    model = Product


class ProductCardDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = self.get_queryset()
        versions = {}
        for product in products:
            current_version = Version.objects.filter(product_id=product.pk, is_current=True)
            if current_version:
                current_version = Version.objects.get(product_id=product.pk, is_current=True)
                versions[product.pk] = current_version
        context_data['current_version'] = versions
        return context_data


class ProductCardDetailView(LoginRequiredMixin, DetailView):
    model = Product
    # template_name = 'catalog/product_card.html'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_продукт'
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.created_by = self.request.user
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.created_by:
            return ProductForm
        if user.has_perms(["catalog.can_cancel_publication",
                           "catalog.can_edit_description",
                           "catalog.can_edit_category"]):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:products')

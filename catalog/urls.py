from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, HomeTemplateView, ProductsListView, ProductCardDetailView, \
    ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductCardDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update')
]

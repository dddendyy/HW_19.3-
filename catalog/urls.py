from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, HomeTemplateView, ProductsListView, ProductCardDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view()),
    path('products/<int:pk>/', ProductCardDetailView.as_view())
]

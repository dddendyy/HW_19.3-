from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products, product_card

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
    path('products/<int:pk>/', product_card)
]

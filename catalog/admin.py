from django.contrib import admin

from catalog.models import Product, Category

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'desc')


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name')

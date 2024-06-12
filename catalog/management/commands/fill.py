from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
             {'name': 'Приправы', 'desc': 'Отлично дополняют любое блюдо'},
             {'name': 'Консеры', 'desc': 'Ну тоже надо'}
        ]

        categories_for_create = []

        for category_item in category_list:
            categories_for_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_for_create)

        product_list = [
            {"name": "Зира (кумин)", "desc": "Самое то для плова", "price": 159, "category": Category.objects.get(pk=8)},
            {"name": "Тушёнка говяжья", "desc": "Без комментариев", "price": 79, "category": Category.objects.get(pk=9)},
        ]

        products_for_create = []

        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)

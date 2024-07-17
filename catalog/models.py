from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    desc = models.TextField(verbose_name='описание')

    def __str__(self):
        return (f"{self.name}\n"
                f"{self.desc}")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    desc = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/', verbose_name='фото', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='произведено')
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name='изменено')

    def __str__(self):
        return (f"{self.name}, {self.price}.\n"
                f"Относится к категории {self.category}\n"
                f"{self.desc}")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='prodict')
    number = models.FloatField(verbose_name='номер')
    name = models.CharField(max_length=30, verbose_name='название версии')
    is_current = models.BooleanField(verbose_name='текущая')

    def __str__(self):
        return f' Версия №{self.number} продукта {self.product}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

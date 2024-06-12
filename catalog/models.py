from django.db import models

# Create your models here.


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

    def  __str__(self):
        return (f"{self.name}, {self.price}.\n"
                f"Относится к категории {self.category}\n"
                f"{self.desc}")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=30, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', null=True, blank=True)
    date = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(verbose_name='опубликовано')
    view_counter = models.IntegerField(verbose_name='кол-во просмотров', default=0)

    def __str__(self):
        return (f'{self.title}\n'
                f'{self.date}\n'
                f'Опубликовано: {self.is_published}\n'
                f'Просмотрено: {self.view_counter} раз(-а)')

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'

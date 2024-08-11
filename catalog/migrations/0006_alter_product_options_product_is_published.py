# Generated by Django 4.2 on 2024-08-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_cancel_publication', 'Can cancel publication'), ('can_edit_description', 'Can edit description'), ('can_edit_category', 'Can edit category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view_counter',
            field=models.IntegerField(blank=True, null=True, verbose_name='кол-во просмотров'),
        ),
    ]

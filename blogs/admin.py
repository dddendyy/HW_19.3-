from django.contrib import admin

from blogs.models import Blog

# Register your models here.


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published', 'view_counter')
    list_filter = ('is_published', 'view_counter')
    search_fields = ('title', 'date')

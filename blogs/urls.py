from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete')
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blogs.models import Blog


# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date', 'is_published')
    success_url = reverse_lazy('blogs:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date', 'is_published')
    success_url = reverse_lazy('blogs:list')


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')

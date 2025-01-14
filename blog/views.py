from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import BlogPost


class CreateBlogPostView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    success_url = reverse_lazy('blog:list')

class ListBlogPostView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'

class DetailBlogPostView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

class UpdateBlogPostView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    template_name_suffix = '_update'
    success_url = reverse_lazy('blog:list')

class DeleteBlogPostView(DeleteView):
    model = BlogPost
    template_name_suffix = '_confirm_delete.html'
    success_url = reverse_lazy('blog:list')
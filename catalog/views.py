from http.client import HTTPResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView, UpdateView
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product



class HomeView(TemplateView):
    template_name = 'catalog/products_list.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsListView(TemplateView):
    template_name = 'catalog/products_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'  # Укажите ваш шаблон
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if not request.user.groups.filter(name='Модератор продуктов').exists() and not request.user == product.owner:
            return HttpResponseForbidden('У вас нет прав для удаления этого продукта')

        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:products_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if not request.user.groups.filter(name='Модератор продуктов').exists() and request.user != product.owner:
            return HttpResponseForbidden('У вас нет прав для редактирования этого продукта')

        return super().dispatch(request, *args, **kwargs)


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('product.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

    # def get_success_url(self):
    #     return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsListView(TemplateView):
    template_name = 'catalog/products_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class ProductDetailView(TemplateView):
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product
        return context
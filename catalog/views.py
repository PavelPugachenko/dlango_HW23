from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_details.html', {'product': product})




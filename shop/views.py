from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from . import models
from .models import Product, Category


def index(request):
    products = Product.objects.all().order_by('-created_at')[:5]
    return render(request, 'products.html', {'products': products})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def single_product(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
        return render(request, 'single_product.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404()


def single_category(request, category_id):
    try:
        products = Product.objects.filter(category_id = category_id)
        category = Category.objects.get(pk = category_id)
        return render(request, 'single_category.html', {'category': category, 'products': products})
    except Product.DoesNotExist:
        raise Http404()
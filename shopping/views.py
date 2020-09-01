from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddForm
from .models import Product, Category


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    page = request.GET.get('page', 1)
    product_paginator = Paginator(products, 3)
    try:
        products_paginated = product_paginator.page(page)
    except PageNotAnInteger:
        products_paginated = product_paginator.page(1)
    except EmptyPage:
        products_paginated = product_paginator.page(product_paginator.num_pages)
    context = {
        'products': products_paginated,
        'categories': categories
    }
    return render(request, 'shopping/home.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm()
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'shopping/product_detail.html', context=context)

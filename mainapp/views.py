import random

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.all()


def index(request):
    contex = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', contex)


def get_hot_product():
    product_ids = Product.objects.values_list('id', flat=True).all()
    product_id = random.choice(product_ids)
    return Product.objects.get(pk=product_id)


def same_product(hot_product):
    return Product.objects.filter(category=hot_product.category). \
               exclude(pk=hot_product.pk)[:3]


def products(request):
    products = Product.objects.all()[:3]
    hot_product = get_hot_product()
    contex = {'page_title': 'продукты',
              'products': products,
              'hot_product': hot_product,
              'same_product': same_product(hot_product),
              'categories': get_menu(), }
    return render(request, 'mainapp/products.html', contex)


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    contex = {'page_title': 'страница товара',
              'product': product,
              'categories': get_menu(), }
    return render(request, 'mainapp/product_page.html', contex)


def category(request, pk):
    page_num = request.GET.get('page', 1)
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    products_paginator = Paginator(products, 3)
    try:
        products = products_paginator.page(page_num)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {'page_title': 'товары категории',
               'products': products,
               'category': category,
               'categories': get_menu()}

    return render(request, 'mainapp/products_category.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': 88003331122,
            'email': 'msk@mail.ru',
            'address': 'В пределах МКАД'
        },
        {
            'city': 'Cанкт-Петербург',
            'phone': 88123331111,
            'email': 'spb@mail.ru',
            'address': 'В пределах КАД'},
        {
            'city': 'Иркутск',
            'phone': 830123333333,
            'email': 'irk@mail.ru',
            'address': 'В пределах центра'}
    ]
    contex = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', contex)

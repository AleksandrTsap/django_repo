from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.all()


def index(request):
    contex = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', contex)


def products(request):
    products = Product.objects.all()[:3]
    product = Product.objects.all()[3]
    contex = {'page_title': 'продукты',
              'products': products,
              'product': product,
              'categories': get_menu(), }
    return render(request, 'mainapp/products.html', contex)


def category(request, pk):
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

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

from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    contex = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', contex)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:3]
    product = Product.objects.all()[3]
    contex = {'page_title': 'продукты',
              'products': products,
              'product': product,
              'categories': categories, }
    return render(request, 'mainapp/products.html', contex)


def category(request, pk):
    print(pk)


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

from django.shortcuts import render
import datetime


def index(request):
    contex = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', contex)


def products(request):
    menu = [{'category': 'все'},
            {'category': 'дом'},
            {'category': 'офис'},
            {'category': 'модер'},
            {'category': 'классика'}, ]
    contex = {
        'page_title': 'продукты',
        'menu': menu,
    }
    return render(request, 'mainapp/products.html', contex)


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

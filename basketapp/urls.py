from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add_to/<int:product_pk>/', basketapp.add_to, name='add_to'),
    path('delete/<int:basket_item_pk>/', basketapp.delete, name='delete'),
    path('update/<int:basket_item_pk>/<int:qty>/', basketapp.update),
]

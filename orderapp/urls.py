from django.urls import path

import orderapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='index'),
    path('create/', ordersapp.OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', ordersapp.OrderUpdate.as_view(), name='update'),
    path('forming_complete/<int:order_pk>/', ordersapp.forming_complete, name='forming_complete')

]

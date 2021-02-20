from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('categories/', adminapp.categories, name='categories'),
    path('user/update/<int:user_pk>', adminapp.user_update, name='user_update'),
    path('user/delete/<int:user_pk>', adminapp.user_delete, name='user_delete'),
]

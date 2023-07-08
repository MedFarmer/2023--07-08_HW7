from django.contrib import admin
from django.urls import path
from .views import index, add_hotel, update_hotel, full_info

urlpatterns = [  
    path('', index, name='index'),
    path('add_hotel/', add_hotel, name='add_hotel'),   
    path('update_hotel/<int:id>', update_hotel, name='update_hotel'),
    path('full_info/<str:name>', full_info, name='full_info'),
]
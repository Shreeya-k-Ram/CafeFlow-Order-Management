from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name = 'menu'),
    path('order/', views.order_view, name = 'order'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('menu/', views.menu_list, name = 'menu'),
    path('order/', views.order_view, name = 'order'),
    path('orders/', views.order_list, name ='orders'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('Order/<int:order_id>/next-status/', views.next_status, name = 'next_status'),
    path("order/<int:order_id>/delete/", views.delete_order, name="delete_order"),

]

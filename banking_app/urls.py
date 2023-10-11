from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('view_customer/<int:customer_id>/', views.view_customer, name='view_customer'),
    path('transfer_money/', views.transfer_money, name='transfer_money'),
]

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('product/',views.product, name="product"),
    path('customer/<int:id>/',views.customer, name="customer"),
    path('create_customer/',views.createCustomer, name="create_customer"),
    path('create_order/',views.createOrder, name="create_order"),
    path('update_order/<int:pk>/',views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>/',views.deleteOrder, name="delete_order"),
]

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('product/',views.product, name="product"),
    path('customer/',views.customer, name="customer"),
]

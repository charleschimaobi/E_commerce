from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_user),
    path('products/', views.index),
    path('products/new/', views.new_products)
]
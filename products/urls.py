from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_user, name = 'greet_user'),
    path('products/', views.index, name = 'index'),
    path('products/new/', views.new_products, name = 'products'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('search/', views.search, name = 'search'),
    path('products/<str:pk>', views.productSearch, name = 'productSearch'),
]
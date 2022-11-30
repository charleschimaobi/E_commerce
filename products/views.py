from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def greet_user(request):
    return HttpResponse('<h1> Hello, Welcome to my e-commerce Platform </h1>' )

products = Product.objects.all()
def index(request):
    return render(request, 'index.html', {'products': products})

def new_products(request):
    return HttpResponse('<h2>Here are our new proucts</h2>')

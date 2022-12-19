from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import Product


def greet_user(request):
    return HttpResponse('<h1> Hello, Welcome to my e-commerce Platform 👋👋😊</h1>' )
    

products = Product.objects.all()
def index(request):
    return render(request, 'index.html', {'products': products})

def new_products(request):
    return HttpResponse('<h2>Here are our new proucts</h2>')

def register(request):
    if request.method == "POST": # ensures that the following happens if a POST request is made
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 == password:
            if User.objects.filter(email = email).exists(): # checks if the entered email already exists
                messages.info(request, 'Email Already Used!')
                return redirect('http://127.0.0.1:8000/register/')
            elif User.objects.filter(username = username).exists(): # checks if the entered username already exists
                messages.info(request, 'Username Already Taken!')
                return redirect('http://127.0.0.1:8000/register/')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)# creates the new user with the following credentials
                user.save()
                return redirect('http://127.0.0.1:8000/login/')
        else:
            messages.info(request, 'Passwords Not Matched!')
            return redirect('http://127.0.0.1:8000/register/')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password) # authenticates the user
        if user is not None: # checks if the user is registered
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/products/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('http://127.0.0.1:8000/login/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/products/')
    
def search(request):
    if request.method =="GET":
        search = request.GET.get("search")
        product = Product.objects.all().filter(name=search)
        return render(request, 'search.html', {'product': product})

def productSearch(request, pk):
    product = Product.objects.get(name=pk)
    return render(request, 'productSearch.html', {'productSearch': product})
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(response):
    return render(response,"accounts/dashboard.html")

def Customer(response):
    return render(response,"accounts/customer.html")

def Products(response):
    return render(response,"accounts/products.html")

def contact(response):
    return HttpResponse("contact")

def about(response):
    return HttpResponse("about")
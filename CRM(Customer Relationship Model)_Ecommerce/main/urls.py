from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("contact/",views.contact),
    path("about/",views.about),
    path("customer/",views.Customer),
    path("products/",views.Products),
]

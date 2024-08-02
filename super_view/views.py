from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Product, Order



class List_view(ListView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

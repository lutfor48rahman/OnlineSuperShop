from django.shortcuts import render

#Import Views
from django.views.generic import ListView,DetailView


#Models
from AppShop.models import Product


#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class Home(ListView):
	model = Product
	template_name = 'AppShop/home.html'



class ProductDetail(LoginRequiredMixin,DetailView):
	model = Product
	template_name = 'AppShop/product_details.html'

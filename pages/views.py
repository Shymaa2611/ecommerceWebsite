from typing import Any, Dict
from django.shortcuts import render
from .models import Product,Product_accessories,Product_Alternative,Category
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView,ListView,DetailView
from .forms import userAccount
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class index(ListView):
    model=Product
    queryset=Product.objects.all()[:10]
    template_name='pages/index.html'
    context_object_name='products'

class profile(DetailView):
    model=Profile
    template_name='User_profile/profile.html'
    context_object_name='data'
    
class edit_profile(UpdateView):
    model=Profile
    form_class=userAccount
    template_name='User_profile/edit_profile.html'
    context_object_name="form"
    success_url='/'

class single_product(DetailView):
    model=Product
    template_name='pages/single_product.html'
    context_object_name='product'

class signUp(CreateView):
    form_class=UserCreationForm
    context_object_name='form'
    template_name='authentication/signUp.html'
    success_url='/'



def forget_passward(request):
    return render(request,'authentication/forget_passward.html')

def reset_passward(request):
    return render(request,'authentication/reset_passward.html')

def cart(request):
    return render(request,'pages/cart.html')

def checkout(request):
    return render(request,'pages/checkout.html')

def order_success(request):
    return render(request,'pages/order_success.html')

def track_order(request):
    return render(request,'pages/track_order.html')
class order(ListView):
    model=Product
    template_name='pages/order.html'
    context_object_name='orders'


       
      



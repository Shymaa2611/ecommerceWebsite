from django.shortcuts import render
from .models import Product,Product_accessories,Product_Alternative,Category
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
def index(request):
    context={
        "products":Product.objects.all(),

    }
    return render(request,'pages/index.html',context)
def profile(request):
    return render(request,'pages/profile.html')
def edit_profile(request):
    return render(request,'pages/edit_profile.html')
def single_product(request,id):
    context={
        "product":Product.objects.get(id=id)
    }
    return render(request,'pages/single_product.html',context)
class signUp(CreateView):
    form_class=UserCreationForm
    context_object_name='form'
    template_name='authentication/signUp.html'
    success_url='/'


def login(request):
    return render(request,'authentication/login.html')

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

def order(request):
    return render(request,'pages/order.html')


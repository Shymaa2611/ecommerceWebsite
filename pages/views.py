from django.shortcuts import render

def index(request):
    return render(request,'pages/index.html')
def profile(request):
    return render(request,'pages/profile.html')
def edit_profile(request):
    return render(request,'pages/edit_profile.html')
def single_product(request):
    return render(request,'pages/single_product.html')
def signUp(request):
    return render(request,'authentication/signUp.html')
def card(request):
    return render(request,'pages/card.html')
def checkout(request):
    return render(request,'pages/checkout.html')
def order_success(request):
    return render(request,'pages/order_success.html')
def login(request):
    return render(request,'authentication/login.html')
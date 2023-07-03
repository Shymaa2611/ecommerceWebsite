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


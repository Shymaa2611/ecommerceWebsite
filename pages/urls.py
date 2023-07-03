from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('single_product/',views.single_product,name='single_product'),
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.login,name='login'),
    path('forget_passward/',views.forget_passward,name='forget_passward'),
    path('reset_passward/',views.reset_passward,name='reset_passward'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('order_success/',views.order_success,name='order_success'),
    path('track_order/',views.track_order,name='track_order'),
    path('order/',views.order,name='order'),
]

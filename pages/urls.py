from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('single_product/<int:id>/',views.single_product,name='single_product'),
    path('signUp/',views.signUp.as_view(),name='signUp'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('login/',auth_view.LoginView.as_view(template_name='authentication/login.html'),name='login'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('order_success/',views.order_success,name='order_success'),
    path('track_order/',views.track_order,name='track_order'),
    path('order/',views.order,name='order'),
    path('forget_passward/', auth_view.PasswordResetView.as_view(template_name='authentication/forget_passward.html'),name='forget_passward'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='authentication/reset_password_done.html'),name='reset_password_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='authentication/reset_passward.html'),name='reset_passward'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),name='password_reset_complete'),
]

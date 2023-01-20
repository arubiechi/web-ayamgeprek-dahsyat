from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('review/',views.review, name='review'),
    path('menu/',views.menu, name='menu'),
    path('register/',views.register, name='register'),
    path('login/',views.login_request, name='login'),
    path('cart/',views.cart,name='cart'),
]
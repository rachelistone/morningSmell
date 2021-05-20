from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('profil/', views.profil, name='profil'),
    path('address/', views.address, name='address-update'),
    path('history/', views.history, name='history'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('about/', views.about, name='about'),
]
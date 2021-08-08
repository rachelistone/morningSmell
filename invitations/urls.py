from django.urls import path, include
from . import views
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('addresses', views.AddressViewSet)

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
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    # path('', include(router.urls)),
    #path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Product, Address
from django.contrib import messages
from django.db import IntegrityError
from .forms import UserRegistrationForm, ContactForm, UserLoginForm, AddressForm, ProdUserAddForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
    content = {}
    return render(request, 'invitations/home.html', content)
    
def products(request):
    if request.method=='GET':
        products_lc = Product.objects.filter(category='לחמניות')
        products_mz = Product.objects.filter(category='מיצים')
        return render(request, 'invitations/products.html', {'products_lc': products_lc, 'products_mz': products_mz, 'form': ProdUserAddForm()})
    else:
        print(request.POST['amount'], request.POST['day'])

def cart(request):
    content = {}
    return render(request, 'invitations/cart.html', content)

def profil(request):
    if Address.objects.filter(user=request.user):
        content = {'address': get_object_or_404(Address, user=request.user), 'addr':1}
        return render(request, 'invitations/profil.html', content)
    else:
        return render(request, 'invitations/profil.html')

def address(request):
    if request.method == 'GET':
        return render(request, 'invitations/address-update.html', {'form': AddressForm()})
    else:
        try:
            form = AddressForm(request.POST)
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('profil')
        except ValueError:
            return render(request, 'invitations/address-update.html', {'form': AddressForm(), 'error':'כתובת לא מתאימה'})

def history(request):
    content = {}
    return render(request, 'invitations/history.html')
    
def checkout(request):
    content = {}
    return render(request, 'invitations/checkout.html', content)
    
def contact(request):
    if request.user.is_authenticated:
        initial = {
            'name': request.user.username,
            'email': request.user.email,
            'phone': request.user.phone
        }
    else:
        initial = None
    if request.method == 'GET':
        return render(request, 'invitations/contact.html', {'form': ContactForm(initial=initial)})
    else:
        try:
            form = ContactForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'invitations/contact.html', {'form': ContactForm(initial=initial)})

    
def usersignup(request):
    if request.method == 'GET':
        return render(request, 'invitations/user-signup.html', {'form': UserRegistrationForm()})
    else:
        # create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],email=request.POST['email'],phone=request.POST['phone'])
                login(request, user)
                return redirect('cart')
            except IntegrityError:
                return render(request, 'invitations/user-signup.html',
                              {'form': UserRegistrationForm(), 'error': 'השם הזה קיים.. נדאג שיאפשר שמות כפולים'})
        else:
            # tell the user that password didnt match
            return render(request, 'invitations/user-signup.html',
                          {'form': UserCreationForm(), 'error': 'הסיסמאות אינם תואמות'})
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'נוצר חשבון עבור{username}')
    #         return redirect('products')
    # return render(request, 'invitations/user-signup.html', {'form': form})

def userlogin(request):
    if request.method == 'GET':
        return render(request, 'invitations/user-login.html', {'form': UserLoginForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'],email=request.POST['email'],phone=request.POST['phone'])
        if user is None:
            return render(request, 'invitations/user-login.html',
                          {'form': UserLoginForm(), 'error': 'שם המשתמש או הסיסמה אינם נכונים.. נסה שוב'})
        else:
            login(request, user)
            return redirect('cart')

def userlogout(request):
    # print(request,'/n')
    # dir(request)
    if request.method == 'POST':
        # if it would be get request, some browsers load the href urls of the page in order to make it faster, then it will log me out without clicking on logout
        logout(request)
        return redirect('home')

def about(request):
    content = {}
    return render(request, 'invitations/about.html', content)

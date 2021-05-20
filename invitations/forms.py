from django import forms
from .models import Contact, Address
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='שם מלא:')
    email = forms.EmailField(label='כתובת מייל:')
    phone_regex = RegexValidator(regex=r'^\d{9,10}$', message="נא הכנס מספר טלפון כולל קידומת")
    phone = forms.CharField(validators=[phone_regex], max_length=10, label='מספר טלפון:', required=False)
    password1 = forms.CharField(label = 'בחר סיסמה:')
    password2 = forms.CharField(label = 'חזור על הסיסמה:')
    class Meta:
        model = User
        fields = ['username', 'email','phone',  'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='שם מלא:')
    email = forms.EmailField(label='כתובת מייל:')
    phone_regex = RegexValidator(regex=r'^\d{9,10}$', message="נא הכנס מספר טלפון כולל קידומת")
    phone = forms.CharField(validators=[phone_regex], max_length=10, label='מספר טלפון:', required=False)
    password = forms.CharField(label='סיסמה:')
    class Meta:
        model = User
        fields = ['username','email', 'phone', 'password']

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='שם מלא:')
    email = forms.EmailField(label='כתובת מייל:')
    phone_regex = RegexValidator(regex=r'^\d{9,10}$', message="נא הכנס מספר טלפון כולל קידומת")
    phone = forms.CharField(validators=[phone_regex], max_length=10, label='מספר טלפון:', required=False)
    title = forms.CharField(label='נושא:')
    message = forms.CharField(widget=forms.Textarea, label='תוכן הפניה:')
    class Meta:
        model = Contact
        fields = ['name','email', 'phone', 'title','message']

class AddressForm(forms.ModelForm):
    town = forms.CharField(label='עיר:')
    street = forms.CharField(label='רחוב:')
    house_num = forms.IntegerField(label='מספר בית:')
    apt_num = forms.IntegerField(label='מספר דירה:')
    level = forms.IntegerField(label='קומה:')
    enter = forms.IntegerField(label='קוד כניסה:', required=False)
    class Meta:
        model = Address
        fields = ['town','street', 'house_num', 'apt_num','level', 'enter']

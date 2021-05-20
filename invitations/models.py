from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as date
from django.conf import settings


class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=30)
    message=models.TextField()
    m_date=models.DateTimeField(auto_now_add=True)#the date massage started no chande when updated

    def __str__(self):
        return f"{self.name}, {self.title}"

#class ExtendUser(User):
#    phone=models.CharField(blank=True, null=True, max_length=10)

User.add_to_class('phone',models.CharField(blank=True, null=True, max_length=10))

class Product(models.Model):
    class Categories(models.TextChoices):
        LH = 'לחמניות'
        HL = 'מוצרי חלב'
        MZ = 'מיצים'
        MA = 'מאפים'

    category = models.CharField(max_length=20, choices=Categories.choices)
    product_name = models.CharField(max_length=30)
    price = models.FloatField()
    picture = models.ImageField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.product_name

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    town = models.CharField(max_length=30, verbose_name='עיר')
    street = models.CharField(max_length=50, verbose_name='רחוב')
    house_num = models.IntegerField(verbose_name='מספר בית')
    apt_num = models.IntegerField(verbose_name='מספר דירה')
    level = models.IntegerField(verbose_name='קומה')
    enter = models.IntegerField(blank=True, null=True, verbose_name='קוד כניסה')

    def get_fields(self):
        for field in Address._meta.fields:
            yield field.verbose_name, field.value_to_string(self)

    def __str__(self):
        return f"{self.town}, {self.street}"

class ProdUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    weekDay = ((6,'SUNDAY'),(0,'MONDAY'),(1,'TUESDAY'),(2,'WEDNESDAY'),(3,'THURSDAY'),(4,'FRIDAY'))

    def get_tmrw():
        weekday=date.now().weekday()
        if weekday==4:
            return weekday+2
        return (weekday+1) % 7

    day = models.IntegerField(default=get_tmrw(), choices=weekDay)
    is_active = models.BooleanField(default=True)
    create_date=models.DateTimeField(auto_now_add=True)
    until_date=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}, {self.product.product_name}"
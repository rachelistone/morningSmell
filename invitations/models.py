from django.db import models
from django.contrib.auth.models import User
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
    Categories = (( 'LH', 'לחמניות'), ('HL','מוצרי חלב'), ('MZ','מיצים') ,  ('MA', 'מאפים'))

    category = models.CharField(max_length=20, choices=Categories)
    product_name = models.CharField(max_length=30)
    price = models.FloatField()
    picture = models.ImageField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.product_name

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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

    weekDay = ((0,'יום ראשון'),(1,'יום שני'),(2,'יום שלישי'),(3,'יום רביעי'),(4,'יום חמישי'),(5,'יום שישי'))

    day = models.IntegerField(choices=weekDay)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}, {self.product.product_name}"

    def price_for_prod(self):
        return self.product.price * self.amount

class BuyHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.product.product_name}"
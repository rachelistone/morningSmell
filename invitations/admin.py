from django.contrib import admin
from .models import Contact, Product, Address, ProdUser
from django.contrib.auth.models import User

class ContactAdmin(admin.ModelAdmin):
    readonly_fields=('m_date',)

class ProdUserAdmin(admin.ModelAdmin):
    readonly_fields=('create_date',)

#class ExtendUserAdmin(admin.ModelAdmin):
    #fields = ('username','password' 'email', 'phone')
    #list_display = ('id', 'username','password' 'email', 'phone',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(ProdUser, ProdUserAdmin)
admin.site.register(Product)
admin.site.register(Address)
admin.site.unregister(User)
admin.site.register(User)
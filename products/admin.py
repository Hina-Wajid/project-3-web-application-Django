from django.contrib import admin
from .models import Product,Offer
#that means from the model module from the current folder

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')    


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')    


admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)

#admin has object named site which has this register method , we pass Product as arg.
#this will be added to our admin panel. this provide all the common functionality needing for admin






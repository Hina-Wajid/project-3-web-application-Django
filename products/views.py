from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

#jango is a package, shortcuts is the module and render is a function that we are going to import.

# Create your views here.

# /products -> index
# url --adress

def index(request):  #main page for your app
    products=Product.objects.all()
    # Product.objects.filter()
    # Product.objects.get()
    # Product.objects.save()

    return render(request,'index.html',
                  {'products':products})


def new(request):
    return HttpResponse('New products')



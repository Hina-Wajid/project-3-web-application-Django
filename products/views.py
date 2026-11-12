from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
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


def detail(request,product_id):
    product=get_object_or_404(Product, id=product_id)  # django will get id from url
    return render(request,'detail.html', {'product':product})

def new(request):
    return HttpResponse('New products')


def home(request):
    return render(request,'home.html')



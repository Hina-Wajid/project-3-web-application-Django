from django.urls import path
from . import views  #from current folder we are importing views
#here we define url for this app/ -view is main view
#/product

urlpatterns =[
path('',views.index,name='products'),
path('new',views.new,name='new'),
path('<int:product_id>/', views.detail, name='product_detail'),


]

#routes to navigate
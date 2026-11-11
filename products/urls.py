from django.urls import path
from . import views  #from current folder we are importing views
#here we define url for this app/ -view is main view
#/product

urlpatterns =[
path('',views.index),
path('new',views.new)

]

#routes to navigate
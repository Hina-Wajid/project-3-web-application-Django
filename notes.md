#
This web application is built using Django framework.
in framework Django 
a library of resuable modules , a framework structures files and folders. for our application

#
# $ pip install django ==2.1



start django server
# $ python manage.py runserver

# view
what should a user see what it navigate to a certain page
views.py is the view for products . by convention index is function name

# urls.py

this where define urls for each package
from . import views  #from current folder we are importing views


urlpatterns

# create a model
we get from database

# migration 
add model and add config in settings.py

 # $ python manage.py makemigrations
this will create 

# $ python manage.py migrate

# admin
by default django comes with admin panel
to create a super user admin .write this

# $ python manage.py createsuperuser
this will prompt you to enter a username, email and password. also will inform you for weak password. 

#add products in admin panel
so in admin.py add products module

# customise admin area
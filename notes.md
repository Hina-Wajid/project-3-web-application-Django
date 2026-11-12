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

# customise admin area -in admin.py


#admin has object named site which has this register method , we pass Product as arg.
#this will be added to our admin panel. this provide all the common functionality needing for admin




# Product.objects.all()
Det er en del af Djangos ORM (Object-Relational Mapping).
Hvad betyder det?
- Product refererer til din model i models.py.
- objects er Djangos manager, som giver adgang til databasen.
- all() henter alle produkter fra databasen.


# get_object_or_404()?
Det er en funktion fra Django, som bruges til at finde et bestemt produkt i databasen.


# Hvordan har du lavet links til produkterne?

## <a href="{% url 'product_detail' product.id %}">
##   View product
## </a>
Her sker følgende:
1. {% url %} finder den URL, du har defineret i urls.py.
2. 'product_detail' er navnet på din URL.
3. product.id sender produktets ID med.
4. Django genererer automatisk det korrekte link.
Fordelen: Hvis du ændrer URL-strukturen i urls.py, behøver du ikke ændre alle dine links manuelt, så længe URL-navnet bevares.
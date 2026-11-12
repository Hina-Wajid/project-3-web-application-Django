# Django Product Website

## 1. About the Project

This project is a website developed using Python and Django.

The purpose of the project was to learn Django, understand how a web framework works, and gain practical experience with backend development, databases, and frontend integration.

The website contains three main pages:

- **Homepage:** The main landing page of the website.
- **Product Page:** Displays products stored in the database.
- **Product Detail Page:** Displays detailed information about an individual product.

The project is not fully populated with products yet, but the main functionality is working.

## 2. Technologies Used

The project uses the following technologies:

 Technology used & Purpose

 Python -- Main programming language 
 Django -- Backend web framework 
 SQLite -- Database 
 HTML -- Website structure 
 CSS  -- Website styling 
 Bootstrap -- Responsive design and frontend components 

## 3. Main Features

### Homepage
The homepage is the main entry point to the website.

### Product Page
The product page retrieves products dynamically from the database using Django ORM.

I use:

```python
Product.objects.all()
```

This retrieves all products from the database.

### Product Detail Page
Users can click on a product to see more information about it.

The product is retrieved using:

```python
get_object_or_404(Product, id=id)
```

This means Django searches for the product using its ID. If the product does not exist, Django returns a 404 error.

### Django Admin
I use Django Admin to manage products.

Products can be created and managed through the administration interface instead of adding them manually to the HTML.

## 4. How the Project Works

The project uses Django's Model-View-Template (MVT) architecture.

- **Model:** Defines the data structure in `models.py`.
- **View:** Handles requests and retrieves data from the database in `views.py`.
- **Template:** Displays the information using HTML templates.

The application uses SQLite to store product information.

Django ORM makes it possible to communicate with the database using Python code instead of writing SQL queries directly.

## 5. URL Routing

Django uses `urls.py` to connect URLs with the correct views.

The product detail page uses the product ID in the URL.

For example:

```text
/products/1/
/products/2/
/products/3/
```

I use Django Template Language with the `{% url %}` tag to generate dynamic links to product detail pages.

## 6. Database and Migrations

The project uses SQLite as its database.

I use Django migrations to update the database when models are changed.

The following commands are used:

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations` creates migration files based on model changes.
- `migrate` applies those changes to the database.

## 7. Installation and Setup

### Requirements

- Python
- pip
- Django

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hina-Wajid/faglig-fornyelse-hina-wajid.git
```

```bash
cd YOUR_PROJECT_FOLDER
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### Step 3: Install Django

```bash
pip install django
```

If the project uses additional Python packages, install those as well.

### Step 4: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create an Admin User

```bash
python manage.py createsuperuser
```

### Step 6: Start the Development Server

```bash
python manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

The Django Admin page is normally available at:

```text
http://127.0.0.1:8000/admin/
```

## 8. Testing

I tested the website manually in the browser.

The tests included:

- Checking that the homepage loads correctly.
- Checking that the product page displays products.
- Checking that clicking on a product opens the correct detail page.
- Checking that product IDs work in the URL.
- Checking that a non-existing product returns a 404 error.

The main functionality worked during testing.

## 9. Challenges and Learning Process

One of the biggest challenges during the project was finding the right learning resources.

There are many Django tutorials available online, and some of them are very long. It was difficult to find tutorials that explained exactly what I needed for my project.

To learn Django, I used different resources, including:

- YouTube tutorials.
- Official Django documentation.
- AI tools such as ChatGPT.
- Experimenting with the code in my own project.

I learned that it is important to compare different resources and use the information to solve practical problems.

## 10. Advantages of Django

I found Django useful because it brings several important parts of web development together.

It provides tools for working with:

- Frontend integration.
- Backend development.
- Database management.
- URL routing.
- Administration through Django Admin.

I especially liked that Django provides a structured way to organize a web application.

This made it easier for me to connect the different parts of my website.

## 11. Limitations and Future Improvements

The website is still a basic version of a product website.

There are several improvements that could be added in the future:

- Add more products to the database.
- Improve the homepage design.
- Add product search and filtering.
- Improve the product detail page.
- Add user authentication.
- Improve testing.

## 12. Conclusion

Through this project, I gained practical experience with Python and Django.

I learned how to create Django models, retrieve information from a database, use Django Admin, work with URL routing, and display dynamic information in HTML templates.

The project helped me understand how frontend, backend, and databases work together in a web application.

Most importantly, I gained experience learning a new technology independently and applying my knowledge to build a working website.

## 13. Resources

- [Official Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Youtube](https://youtube.com/)

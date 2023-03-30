# README

This is a sample project called "mastiflex_project" that showcases a simple website built using Django. The project structure follows the standard Django project layout.

## Project structure
```
mastiflex_project/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mastiflex/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mastiflex_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── fonts/
│   ├── img/
│   └── js/
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── products.html
    ├── news.html
    ├── contact.html
    ├── accounts/
    │   ├── dasboard.html
    │   ├── login.html
    │   ├── logout.html
    │   └── singup.html
    └── partials/
        ├── _footer.html
        ├── _header.html
        └── _navbar.html
``` 
The project consists of the following apps:

- **mastiflex_app**: The main app that contains the views for the website's main pages.
- **accounts**: An app that provides authentication functionality such as user signup, login, and logout.

The project also contains a **static** directory which contains CSS, fonts, images, and JavaScript files used by the website, and a **templates** directory that contains HTML templates used by the app.

## Files

### File - templates/base.html:
```
{% load static %}

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>{% block title %}{% endblock %}</title>
	<link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
	{% include 'partials/_header.html' %}
	{% include 'partials/_navbar.html' %}

	<main>
		{% block content %}
		{% endblock %}
	</main>

	{% include 'partials/_footer.html' %}
</body>
</html>
```
### File - templates/index.html:
```
{% load static %}

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>{% block title %}{% endblock %}</title>
	<link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
	{% include 'partials/_header.html' %}
	{% include 'partials/_navbar.html' %}

	<main>
		{% block content %}
		{% endblock %}
	</main>

	{% include 'partials/_footer.html' %}
</body>
</html>
```
### File - templates/about.html:
```
{% extends 'base.html' %}

{% block content %}
    <h1>About Mastiflex</h1>
    <p>Mastiflex is a leading manufacturer of adhesive polyurethane sealants, with over 20 years of experience in the industry.</p>
    <p>Our products are used in a variety of applications, from construction to automotive and marine industries.</p>
{% endblock %}
```
### File - templates/products.html:
```
{% extends 'base.html' %}

{% block content %}
  <h1>Products</h1>
  {% for product in products %}
    <div class="product">
      <h2>{{ product.name }}</h2>
      <p>Colors: {{ product.colors }}</p>
      <p>Packaging: {{ product.packaging }}</p>
      <p>Category: {{ product.category }}</p>
      <p>Description: {{ product.description }}</p>
    </div>
  {% endfor %}
{% endblock %}
```
### File - templates/news.html:
```
{% extends 'base.html' %}

{% block content %}
    <h1>News</h1>
    <h2>Latest News</h2>
    <p>Check out our latest product releases and company news.</p>
    <h2>Press Releases</h2>
    <p>Read our latest press releases and media coverage.</p>
{% endblock %}
```
### File - templates/contact.html:
```
{% extends 'base.html' %}

{% block content %}
    <h1>Contact Us</h1>
    <p>Feel free to get in touch with us for any questions, inquiries or comments you may have.</p>
    <ul>
        <li>Email: info@mastiflex.com</li>
        <li>Phone: +1 555 555 5555</li>
        <li>Address: 123 Main Street, Anytown, USA</li>
    </ul>
{% endblock %}
```
### File - templates/partials/_navbar.html:
```
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'index' %}">Mastiflex</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'index' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'about' %}">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'products' %}">Products</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'news' %}">News</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'contact' %}">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
### File - templates/partials/_header.html:
```
<header>
	<h1>My Website</h1>
</header>

### File - templates/partials/_footer.html:
<footer>
	<p>&copy; My Website 2023. All Rights Reserved.</p>
</footer>
```
### File - templates/accounts/dashboard.html:
```
{% block title %}
    Dashboard
{% endblock %}

{% block content %}
    <h1>Welcome {{ user.username }}</h1>
{% endblock %}
```
### File - templates/accounts/login.html:
```
{% extends 'base.html' %}

{% block content %}
  <h2>Login</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
{% endblock %}
```
### File - templates/accounts/logout.html

### File - templates/accounts/signup.html:
```
{% extends 'base.html' %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
```
### File - style.css:
```
/* Global styles */
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

body {
	font-family: Arial, sans-serif;
	font-size: 16px;
	line-height: 1.5;
	color: #333;
	background-color: #f7f7f7;
}

header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 20px;
	background-color: #2F6EA7;
	color: #fff;
}

header h1 {
	font-size: 32px;
}

nav ul {
	display: flex;
	list-style: none;
}

nav li {
	margin-left: 20px;
}

nav a {
	color: #fff;
	text-decoration: none;
}

nav a:hover {
	text-decoration: underline;
}

main {
	max-width: 800px;
	margin: 0 auto;
	padding: 40px 20px;
}

.hero {
	background-color: #EE4150;
	padding: 60px;
	color: #fff;
	text-align: center;
}

.hero h2 {
	font-size: 48px;
	margin-bottom: 20px;
}

.hero p {
	font-size: 24px;
	margin-bottom: 40px;
}

.btn {
	display: inline-block;
	padding: 10px 20px;
	background-color: #2F6EA7;
	color: #fff;
	border-radius: 5px;
	text-decoration: none;
}

.btn:hover {
	background-color: #fff;
	color: #2F6EA7;
}

.services {
	padding: 60px;
	background-color: #fff;
	text-align: center;
}

.services h2 {
	font-size: 32px;
	margin-bottom: 40px;
}

.services ul {
	display: flex;
	justify-content: space-between;
	align-items: stretch;
	list-style: none;
	margin-bottom: 40px;
}

.services li {
	flex-basis: calc(33.33% - 40px);
	background-color: #f7f7f7;
	padding: 20px;
	border-radius: 5px;
	box-shadow: 0 5px 10px rgba(0,0,0,0.1);
}

.services li h3 {
	font-size: 24px;
	margin-bottom: 20px;
}

.services li p {
	font-size: 16px;
}

.about {
	padding: 60px;
	background-color: #2F6EA7;
	color: #fff;
	text-align: center;
}

.about h2 {
	font-size: 32px;
	margin-bottom: 40px;
}

.about p {
	font-size: 16px;
	margin-bottom: 40px;
}

footer {
	padding: 20px;
	background-color: #2F6EA7;
	color: #fff;
	text-align: center;
}

/* Navbar styles */
nav.navbar {
	background-color: #f7f7f7;
	border-bottom: 1px solid #ddd;
}

nav.navbar a.navbar-brand {
	color: #333;
	font-weight: bold;
}

nav.navbar ul.navbar-nav li.nav-item {
	margin-left: 10px;
}

nav.navbar ul.navbar-nav li.nav-item a.nav-link {
	color: #333;
	font-weight: bold;
}

nav.navbar ul.navbar-nav li.nav-item a.nav-link:hover {
	color: #EE4150;
}
```
### File - mastiflex/__init__.py:

### File - mastiflex/asgi.py:
```
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mastiflex.settings')

application = get_asgi_application()
```
### File - mastiflex/settings.py:
```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@y+0kos0_dxx&&d$%_v^63w&gh1mcg+*=n@-z_#4tp1!wv48xk'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mastiflex_app',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mastiflex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # added this line to specify template directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mastiflex.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/' # added slash before static for correct URL mapping
STATICFILES_DIRS = [BASE_DIR / 'static'] # added this line to specify static directory

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
### File - mastiflex/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mastiflex_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
```
### File - mastiflex/wsgi.py:
```
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mastiflex.settings')

application = get_wsgi_application()
```
### File - mastiflex_app/__init__.py:

### File - mastiflex_app/admin.py:

### File - mastiflex_app/apps.py:
```
from django.apps import AppConfig


class MastiflexAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mastiflex_app'
```
### File - mastiflex_app/models.py:
```
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    colors = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
```
### File - mastiflex_app/tests.py:

### File - mastiflex_app/urls.py:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]
```
### File - mastiflex_app/views.py:
```
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')
```
### File - accounnts/__init__.py:

### File - accounnts/admin.py:

### File - accounnts/apps.py:
```
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
```
### File - accounnts/forms.py:
```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```
### File - accounnts/models.py:

### File - accounnts/tests.py:

### File - accounnts/urls.py:
```
from django.urls import path
from .views import dashboard, login_view, logout_view, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
```
### File - accounnts/views.py:
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
```

## Usage

To run the project, make sure you have Python installed. Then, navigate to the project directory in the terminal and run the following command:

`python manage.py runserver`

This will start the development server on `http://localhost:8000/`.

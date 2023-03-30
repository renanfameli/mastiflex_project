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

## Usage

To run the project, make sure you have Python installed. Then, navigate to the project directory in the terminal and run the following command:

`python manage.py runserver`

This will start the development server on `http://localhost:8000/`.

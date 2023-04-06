from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/add/', views.add_product, name='add_product'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]

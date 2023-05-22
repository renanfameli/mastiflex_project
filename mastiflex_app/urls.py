from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>/', views.products, name='products_by_category'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
]

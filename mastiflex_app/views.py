from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'add_product.html', context)

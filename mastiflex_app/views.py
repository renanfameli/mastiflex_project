from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


def index(request):
    context = {
        'selected_page': 'index',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'selected_page': 'about',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'selected_page': 'contact',
    }
    return render(request, 'contact.html', context)


def products(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products_list = Product.objects.filter(category=selected_category)
    else:
        selected_category = None
        products_list = Product.objects.all()
    context = {'categories': categories,
               'products': products_list,
               'selected_category': selected_category,
               'selected_page': 'products'
               }
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def news(request):
    context = {
        'selected_page': 'news',
    }
    return render(request, 'news.html', context)


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

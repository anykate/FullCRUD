from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('products:list_products')

    return render(request, 'products/create_update_product.html', {'form': form})


def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('products:list_products')

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products:list_products')

    return render(request, 'products/create_update_product.html', {'form': form})


def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('products:list_products')

    if request.method == 'POST':
        if "submit" in request.POST:
            product.delete()

        return redirect('products:list_products')

    return render(request, 'products/product-delete-confirmation.html', {'product': product})


def details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('/')

    return render(request, 'products/details_product.html', {'product': product})

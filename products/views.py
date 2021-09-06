from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.
from django.shortcuts import render


def all_trips(request):
    """ A view to show all space trips """

    trips = Product.objects.all().filter(category__name='trip')

    context = {
        'trips': trips,
    }
    return render(request, 'products/trips.html', context)

def all_products(request):
    """ A view to show all products without space trips """

    products = Product.objects.all().exclude(category__name='trip')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
from django.shortcuts import render
from products.models import Product

def index(request):
    """ A view to return the index page """

    products = Product.objects.all().exclude(category__name='trip').order_by('id')[:5]

    context = {
        'products': products,
      }
    return render(request, 'home/index.html', context)


# class Trips: zoals webhookhandler
#    def __init__(self, product)

#   def get_trip(self, request):
#       """ A view to return the index page """

#       products = Product.objects.all().filter(category__name='trip')

#       context = {
#         'products': products,
#       }

#       return render(request, 'home/index.html', context)
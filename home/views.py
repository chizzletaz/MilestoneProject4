from django.shortcuts import render
# from products.models import Product

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# class Trips: zoals webhookhandler
#    def __init__(self, product)

#   def get_trip(self, request):
#       """ A view to return the index page """

#       products = Product.objects.all().filter(category__name='trip')

#       context = {
#         'products': products,
#       }

#       return render(request, 'home/index.html', context)
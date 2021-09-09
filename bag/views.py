from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def view_bag(request):
    """ A view that renderes the bag content """

    return render(request, 'bag/bag.html')

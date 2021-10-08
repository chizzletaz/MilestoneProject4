from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag content """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specific product to the shopping bag """

    # product = get_object_or_404(Product, pk=item_id)
    # quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    # bag = request.session.get('bag', {})
    
    # if item_id in list(bag.keys()):
    #     bag[item_id]['quantity'] += quantity['quantity']
    #     messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}.')
    # else:
    #     bag[item_id] = quantity
    #     if request.POST.get('departure') is not None:
    #         departure = request.POST.get('departure')
    #         bag[item_id] = {'quantity': quantity, 'departure': departure}
    #     messages.success(request, f'Added {product.name} to your bag.')
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    departure = None
    if 'departure' in request.POST:
        departure = request.POST['departure']
    bag = request.session.get('bag', {})
    
    # if it is a trip, so with departure
    if departure:
        if item_id in list(bag.keys()):
            if departure in bag[item_id]['items_by_departure'].keys():
                bag[item_id]['items_by_departure'][departure] += quantity
                messages.success(request, f'Updated {product.name} @ {departure} to {bag[item_id][departure]}.')
            else:
                bag[item_id]['items_by_departure']['departure'] = quantity
                messages.success(request, f'Added {product.name} @ {departure} to your bag.')
        else:
            bag[item_id] = {'items_by_departure': {departure: quantity}}
            messages.success(request, f'Added {product.name} @ {departure} to your bag.')
    # if it is a product, so without departure
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag.')

    
    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specific product to the specific amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    departure = None
    if 'departure' in request.POST:
        departure = request.POST['departure']
    bag = request.session.get('bag', {})

    # if it is a trip, so with departure
    if departure:
        if quantity > 0:
            bag[item_id]['items_by_departure'][departure] = quantity
            messages.success(request, f'Updated {product.name} @ {departure} to {bag[item_id]["items_by_departure"][departure]}.')
        else:
            del bag[item_id]['items_by_departure'][departure]
            if not bag[item_id]['items_by_departure']:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} @ {departure} from your bag')
    # if is is a product, so without departure
    else:    
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}.')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    # try:
    #     product = get_object_or_404(Product, pk=item_id)
    #     bag = request.session.get('bag', {})

    #     bag.pop(item_id)
    #     messages.success(request, f'Removed {product.name} from your bag.')

    #     request.session['bag'] = bag
    #     return HttpResponse(status=200)
        
    # except Exception as e:
    #     messages.error(request, f'Error removing item: {e}')
    #     return HttpResponse(status=500)

    
    try:
        product = get_object_or_404(Product, pk=item_id)
        departure = None
        if 'departure' in request.POST:
            departure = request.POST['departure']
        bag = request.session.get('bag', {})

        # if it is a trip, so with departure
        if departure:
            del bag[item_id]['items_by_departure'][departure]
            if not bag[item_id]['items_by_departure']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} @ {departure} from your bag')
        # if is is a product, so without departure
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
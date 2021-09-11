from .forms import OrderForm
from django.shortcuts import redirect, render, reverse
from django.contrib import messages


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51JNfSdGgVZ9GzB4oVdpwygdOom03580pvEGhHESX7v6hAbarUrMDYw2126xEDouYuoeQ5z2RPBkhtfR4oWTOmGIW00dVNAek25",
        'client_secret': "test client secret",
    }

    return render(request, template, context)

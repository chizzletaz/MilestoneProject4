from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    contact_form = ContactForm

    context = {
        'form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    """ A view to return the contact page """
    

    if request.method == "POST":
        contact_form = ContactForm(request.POST) 
        if contact_form.is_valid():
            cust_email = request.POST['email'],
            # credit for using cleaned_data https://docs.djangoproject.com/en/3.2/ref/forms/validation/
            subject = ('We have receiced your message with subject: ' +
                       contact_form.cleaned_data['message_subject'])
            body = render_to_string('contact/confirmation_emails/confirmation_email_body.txt',
                    {'contact_form': contact_form, 'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email],
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact'))

    contact_form = ContactForm

    context = {
        'form': contact_form,
        'on_profile_page': True,
    }

    return render(request, 'contact/contact.html', context)
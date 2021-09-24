from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    """ A view to return the contact page """
    

    if request.method == "POST":
        # form_data = {
        #     'full_name': request.POST['full_name'],
        #     'email': request.POST['email'],
        #     'message_subject': request.POST['message_subject'],
        #     'message_body': request.POST['message_body'],
        # }
        # order_form = contact_form(form_data)
        contact_form = ContactForm(request.POST) 
        if contact_form.is_valid():
            cust_email = request.POST['email'],
            subject = ('We have receiced your message with subject: ' +
                       contact_form.cleaned_data['message_subject'])
            body = render_to_string('contact/confirmation_emails/confirmation_email_body.txt',
                    {'contact_form': contact_form, 'contact_email': settings.DEFAULT_FROM_EMAIL})

            print(cust_email, subject, body)
            # send_mail(
            #     subject,
            #     body,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [cust_email]
            # )
            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact'))

    contact_form = ContactForm

    context = {
        'form': contact_form,
        'on_profile_page': True,
    }

    return render(request, 'contact/contact.html', context)
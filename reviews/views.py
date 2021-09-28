from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages


from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile

def add_review(request, product_id):
    """ A view that lets a logged in user to add a review """
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        user = UserProfile.objects.get(user=request.user)
        if not request.user:
            messages.error(request, 'Sorry, only logged in users can leave a review.')
            return redirect(reverse('login'))

        if request.user.is_authenticated:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.user = user
                review.save()
                messages.success(request, 'Review succesfully added!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add review. Please ensure the form is valid.')

    review_form = ReviewForm

    context = {
        'form': review_form,
        'on_profile_page': True,
    }

    return render(request, 'review/add_review.html', context)

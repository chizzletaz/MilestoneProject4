from django.db.models.aggregates import Avg
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """ Add a review to a product/trip """

    if request.user.is_authenticated:
        if request.method == "POST":
            product = get_object_or_404(Product, pk=product_id)
            user = UserProfile.objects.get(user=request.user)
            review_form = ReviewForm(request.POST)
            print(review_form)
            # check if user already added a review
            added_review = Review.objects.filter(user=user, product=product)
            if added_review.exists():
                
                messages.error(request, 'You already reviewed this product. To change your review click the edit button on your review.')
            else:
                if review_form.is_valid():
                    print('1 test')
                    review = review_form.save(commit=False)
                    review.product = product
                    review.user = user
                    review.save()

                    # Recalculate rating
                    reviews = Review.objects.filter(product=product)
                    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
                    product.rating = average_rating
                    product.save()
    
                    messages.success(request, 'Review succesfully added!')
                else:
                    print('This works')
                    messages.error(request, 'Failed to add review. Please ensure the form is valid.')
            return redirect(reverse('product_detail', args=[product.id]))
        
        # else:
        #     review_form = ReviewForm()

        # template = 'products/product_details.html'
        # context = {
        #     'form': review_form,
        #     'on_profile_page': True,
        # }

        # return render(request, template, context)

    else:
        messages.error(request, 'Sorry, only logged in users can leave a review.')
        return redirect(reverse('login'))




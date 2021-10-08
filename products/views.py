from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products without space trips """

    products = Product.objects.all().exclude(category__name='trip')
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product details """

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
    else:
        user = None
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm()

    # Check if user has already added a review
    try:
        previous_review = Review.objects.get(user=user, product=product)
        review_edit_form = ReviewForm(instance=previous_review)
        
    except:
        review_edit_form = None

    context = {
        'product': product,
        'reviews': reviews,
        'form': review_form,
        'review_edit_form': review_edit_form,
    }

    return render(request, 'products/product_detail.html', context)


def all_trips(request):
    """ A view to show all space trips """

    products = Product.objects.all().filter(category__name='trip').order_by('price')

    context = {
        'products': products,
    }
    return render(request, 'products/trips.html', context)


def trip_detail(request, product_id):
    """ A view to show an individual trip details """

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
    else:
        user = None
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm()

    # Check if user has already added a review
    try:
        previous_review = Review.objects.get(user=user, product=product)
        review_edit_form = ReviewForm(instance=previous_review)
        
    except:
        review_edit_form = None

    context = {
        'product': product,
        'reviews': reviews,
        'form': review_form,
        'review_edit_form': review_edit_form,
    }

    return render(request, 'products/trip_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to take this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            if product.category.name == 'trip':
                return redirect(reverse('trip_detail', args=[product.id]))
            else:
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to take this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            if product.category == 'Trip':
                return redirect(reverse('trip_detail', args=[product.id]))
            else: 
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to take this action.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
"""
This script allows user to view, add, adjust and delete reviews
"""
from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from reviews.models import Review
from products.models import Product
from profiles.models import UserProfile
from .forms import ReviewForm

# Create your views here.


def review_list(request, product_id):

    """function to view the reviews"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request,'products/product_detail.html', context)

def add_review(request, product_id):

    """to add reviews"""

    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.title = request.POST['title']
                form.comment = request.POST['comment']
                form.user = UserProfile.objects.get(user=request.user)
                form.product = product
                form.save()
                messages.success(request, 'You successfully added review!')
                return redirect('product_detail', product_id)
        else:
            form = ReviewForm()
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        messages.error(request, 'Sorry, only login user can do that.')
        return redirect('home')

@login_required
def edit_review(request, product_id, review_id):
    """Function to edit reviews"""

    if request.user.is_authenticated:
        product = Product.objects.get (pk=product_id)
        review = Review.objects.get(product=product, pk=review_id)

        if request.user.userprofile == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.save()
                    messages.success(request, 'You successfully edited review!')
                    return redirect('product_detail', product_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'reviews/edit_review.html', {'form':form})
        else:
            messages.error(request, 'Sorry, only review owner can do that.')
            return redirect('product_detail', product_id)
    else:
        return redirect('home')


@login_required
def delete_review(request, product_id, review_id):
    """Function to edit reviews"""

    if request.user.is_authenticated:
        product = Product.objects.get (pk=product_id)
        review = Review.objects.get(product=product, pk=review_id)

        if request.user.is_superuser:
            review.delete()
            messages.success(request, 'You successfully deleted your review!')

        return redirect('product_detail', product_id)
    else:
        return redirect('home')

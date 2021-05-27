"""
This script allows yser to add to and remove from favourites
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile



# Create your views here.

@login_required
def favourites(request, product_id):
    """
    This function adds products to favourites
    """

    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def product_favourite_list(request):
    """
    This function renders favourite products
    """
    user=request.user
    favourite_products = user.favourites.all()

    context = {
        'is_favourite': favourite_products
    }

    return render(request, 'favourites/product_favourite_list.html', context)

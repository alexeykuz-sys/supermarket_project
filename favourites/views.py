from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile


from django.conf import settings

# Create your views here.

@login_required
def favourites(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if product.favourites.filter(id=request.user.ide).exist():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
        
    
    return render(request, 'favourites/favourites.html')


def product_favourite_list(request):
    user=request.user
    favourite_products = user.favourite.all()
    
    context = {
        'favourite_products': favourite_products
    }

    return render(request, 'favourites/favourites.html', context)
    